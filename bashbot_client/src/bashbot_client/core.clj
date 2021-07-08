(ns bashbot-client.core
  (:require [clj-http.client :as client]
            [cheshire.core :refer :all]
            [clojure.string :as str])
  (:use [clojure.java.shell :only [sh]])
  (:gen-class))

(def welcome-text 
  "Hello, I am BashBot. I can help you learning the bash shell: \n - Ask me how to do something in the bash shell \n - Ask me about a quiz")

(defn escape [message] (str/replace message #"\"" ""))
(defrecord RasaPayload [sender message])
(defn make-rasa-payload ([sender message]
                         (->RasaPayload sender (escape message))))

(def rasa-url "http://localhost:3000/webhooks/rest/webhook/")
(def rasa-url-proxied "http://localhost/webhooks/rest/webhook/")

(defn build-json-payload [rasa-payload] 
  (cheshire.core/generate-string rasa-payload))

(defn query-bashbot
  "Get next message from rasa"
  [url rasa-payload]
  (:body (client/post url {:body (build-json-payload rasa-payload)
                           :headers {"Content-Type" "application/json"}})))

(defn is-exit-command? [command] (some #(= command %) [":q" "exit" "stop" "quit"]))
(def is-not-exit-command? (complement is-exit-command?))
(defn to-regular-array [x] (reduce conj [] x))
(defn extract-answer [answer] (map #(:text %1) (cheshire.core/parse-string answer true)))
(defn filter-execute [answer] (str/replace answer #"EXECUTE" "I executed"))
(defn filter-answers [answers] (map filter-execute answers)) ; This is stupid. hook will not work any more
(defn print-answers [answers] (print "\n=> ") (run! println answers) answers)

(def client-id (str "cli-client-" (rand-int 100000)))

(defn get-answer-from-bot [query-func hook user-message]
  (-> (query-func (make-rasa-payload client-id user-message))
      extract-answer
      to-regular-array
      filter-answers
      print-answers
      hook))

(defrecord CommandData [command payload])
(defn make-command-data ([command payload]
  (->CommandData command payload)))

(defn execute-command [command-data]
  (let [command-type (:command command-data)
        payload (:payload command-data)
        is #(= command-type %1)] 
  (println (cond
    (is "mkdir")  (:out (sh "mkdir" payload))
    (is "cd")     (:out (sh "cd" payload))
    (is "cat")    (:out  (sh "cat" payload))
    (is "rm")     (:out (sh "rm" payload))
    (is "rmrf") (:out (sh "rm" "-rf" payload))
    (is "ls")     (:out (sh "ls"))
    (is "touch")  (:out (sh "touch" payload))
    :else         "Unknown command"))))

(defn is-execute-response? [message] (str/starts-with? message "I executed"))

(defn to-command-data [commands] 
  (make-command-data (nth commands 2) (nth commands 3)))

(defn extract-command-and-keyword [message] 
  (-> (str/split message #"\s")
      to-command-data))

(defn hook [messages] 
  (if (empty? messages)
  messages
  (cond
    (is-execute-response? (first messages)) (-> (first messages)
                                       extract-command-and-keyword
                                       execute-command)
    :else messages)))

(defn get-answer-from-local-bot
  [user-message]
  (get-answer-from-bot (partial query-bashbot rasa-url-proxied) hook user-message))

(defn chat-loop
  [reader get-answer]
  (loop [user-message (reader)]
    (when (is-not-exit-command? user-message)
      (get-answer user-message)
      (recur (reader)))))

(def is-debug? false)

(defn -main
  "Basbhot cli client"
  [& args]
  (try
    (do (println welcome-text)
    (chat-loop read-line get-answer-from-local-bot))
    (catch Exception e (if is-debug?
                         (println e)
                         (println "Something bad happened... Shutting down")))
    (finally (System/exit 0))))
    