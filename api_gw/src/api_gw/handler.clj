(ns api-gw.handler
  (:require [compojure.core :refer :all]
            [compojure.route :as route]
            [ring.middleware.defaults :refer [wrap-defaults site-defaults]]
            [ring.middleware.json :refer [wrap-json-body]]
            [clojure.string :as str]
            [cheshire.core :refer :all]
            [clj-http.client :as client]))

(def rasa-url "http://localhost:5005/webhooks/rest/webhook/")
(def rasa-url-container "http://rasa:5005/webhooks/rest/webhook/")

(defn build-json-payload [client-name message]
  (str "{\"sender\": \"" client-name "\", \"message\": \"" message "\"}"))
(defn to-rasa-server [sender message]
  (let [json-payload (build-json-payload sender message)]
    (println json-payload)
    (:body (client/post rasa-url-container {:body json-payload}))))

(defn send-no-to-rasa [sender] (to-rasa-server sender "No"))

(def should-execute-message "Should I execute this command?")

(defn build-filtered-message [parsed]
  (str "[{\"recipient_id\": \"" (:recipient_id parsed) "\", \"text\": " (:text parsed) "}]"))

(defn filter-execute-message [sender messages]
  (let [parsed (cheshire.core/parse-string messages true)]
   (if (= (:text (last parsed)) should-execute-message)
     (do
      (send-no-to-rasa sender)
      (println (build-filtered-message (first parsed)))
      (build-filtered-message (first parsed)))
     messages)))

(defn forward [req]
  (let [sender (get-in req  [:body "sender"])
        message (get-in req  [:body "message"])
        is-cli-client (str/starts-with? sender "cli")
        rasa-answer (to-rasa-server sender message)]
    (println rasa-answer)
    (if is-cli-client
      rasa-answer
      (filter-execute-message sender rasa-answer))))

(defroutes app-routes
  (POST "/webhooks/rest/webhook/" req (forward req))
  (route/not-found "Not Found"))

(def app
  (wrap-json-body 
    app-routes
    (assoc-in site-defaults [:security :anti-forgery] false)))
