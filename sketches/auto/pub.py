import paho.mqtt.client as mqtt
import sys
import time

client = mqtt.Client(sys.argv[1])
client.connect(sys.argv[2])
client.publish("master", sys.argv[3])
while True:
    client.publish(sys.argv[3], "OK")
    time.sleep(5)

client.disconnect()
