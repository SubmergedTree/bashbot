(ns bashbot-client.core
  (:require [clj-http.client :as client]
            [cheshire.core :refer :all]
            [clojure.string :as str])
  (:use [clojure.java.shell :only [sh]])
  (:gen-class))

(def welcome-text 
  "Hello, I am BashBot. I can help you learning the bash shell: \n - Ask me how to do something in the bash shell \n - Ask me about a quiz")

(defrecord RasaPayload [client-name message])
(defn make-rasa-payload ([client-name message]
                         (->RasaPayload client-name message)))

(def rasa-url "http://localhost:3000/webhooks/rest/webhook/")
(defn build-json-payload [rasa-payload]
  (str "{\"sender\": \""(:client-name rasa-payload)"\", \"message\": \""(:message rasa-payload)"\"}"))

(defn query-bashbot
  "Get next message from rasa"
  [url rasa-payload]
  (:body (client/post url {:body (build-json-payload rasa-payload)
                           :headers {"Content-Type" "application/json"}})))

(defn is-exit-command? [command] (some #(= command %) [":q" "exit" "stop" "quit"]))
(def is-not-exit-command? (complement is-exit-command?))
(defn to-regular-array [x] (reduce conj [] x))
(defn extract-answer [answer] (map #(:text %1) (cheshire.core/parse-string answer true)))
(defn print-answers [answers] (print "=> ") (run! println answers) answers)

; TODO filter out EXECUTE command payload before printing

; TODO hook function which is called after print answers with parameter response from bot to do local analysis
(defn get-answer-from-bot [query-func hook user-message]
  (-> (query-func (make-rasa-payload "cli-client-01" user-message))
      extract-answer
      to-regular-array
      print-answers
      hook))

(defrecord CommandData [command payload])
(defn make-command-data ([command payload]
  (->CommandData command payload)))

(defn execute-command [command-data]
  (let [command-type (:command command-data)
        payload (:payload command-data)
        is #(= command-type %1)] 
  (cond
    (is "mkdir")  (:out (sh "mkdir" payload))
    (is "cd")     (:out (sh "cd" payload))
    (is "cat")    (:out (sh "cat" payload))
    (is "rm")     (:out (sh "rm" payload))
    (is "rm -rf") (:out (sh "rm -rf" payload))
    (is "ls")     (:out (sh "ls"))
    (is "touch")  (:out (sh "touch" payload))
    :else         "Unknown command")))

(defn is-execute-response? [message] (str/starts-with? message "EXECUTE"))

(defn to-command-data [commands] 
  (make-command-data (nth commands 1) (nth commands 2)))

(defn extract-command-and-keyword [message] 
  (-> (str/split message #"\s")
      to-command-data))

(defn hook [messages] 
  (cond
    (is-execute-response? (first messages)) (-> (first messages)
                                       extract-command-and-keyword
                                       execute-command)
    :else messages))

(defn get-answer-from-local-bot
  [user-message]
  (get-answer-from-bot (partial query-bashbot rasa-url) hook user-message))

(defn chat-loop
  [reader get-answer]
  (loop [user-message (reader)]
    (when (is-not-exit-command? user-message)
      (get-answer user-message)
      (recur (reader)))))


(defn -main
  "Basbhot cli client"
  [& args]
  (do (println welcome-text) 
      (chat-loop read-line get-answer-from-local-bot) 
      (System/exit 0))) ; to close thread pool used by sh
