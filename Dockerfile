#FROM rasa/rasa:latest
#COPY . /bashbot

FROM nginx:latest
COPY webclient /usr/share/nginx/html
