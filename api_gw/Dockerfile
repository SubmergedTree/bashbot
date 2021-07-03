FROM openjdk:latest

RUN mkdir -p /app 
COPY target/*-standalone.jar .

CMD java -jar api_gw-0.1.0-SNAPSHOT-standalone.jar
EXPOSE 3000
