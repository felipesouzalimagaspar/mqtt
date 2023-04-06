FROM ubuntu:latest

RUN apt-get update && apt-get install -y mosquitto mosquitto-clients python3 python3-pip redis-server

RUN pip3 install paho-mqtt redis

CMD service redis-server start & mosquitto -c /etc/mosquitto/mosquitto.conf & python3
