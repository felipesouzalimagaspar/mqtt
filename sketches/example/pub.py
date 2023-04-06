import paho.mqtt.client as mqtt
import sys

client = mqtt.Client(sys.argv[1])
client.connect(sys.argv[2])
client.publish(sys.argv[3], sys.argv[4])
client.disconnect()
