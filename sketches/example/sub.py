import paho.mqtt.client as mqtt
import sys

def on_connect(client, userdata, flags, rc):
    print("Connected")
    client.subscribe(sys.argv[3])

def on_message(client, userdata, message):
    print("Listenning: " + str(message.payload.decode()))

client = mqtt.Client(sys.argv[1])
client.on_connect = on_connect
client.on_message = on_message
client.connect(sys.argv[2])
client.loop_forever()
