import paho.mqtt.client as mqtt
import sys

def on_connect(client, userdata, flags, rc):
    print("Connected")
    client.subscribe("master")

def on_message(client, userdata, message):
    if(message.topic == "master"):
        print("Connecting: " + str(message.payload.decode()))
        client.subscribe(str(message.payload.decode()))
    else:
        print("Listenning: " + message.topic + " - " + str(message.payload.decode()))

client = mqtt.Client(sys.argv[1])
client.on_connect = on_connect
client.on_message = on_message
client.connect(sys.argv[2])
client.loop_forever()
