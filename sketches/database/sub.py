import paho.mqtt.client as mqtt, sys, redis, datetime, json

r = redis.Redis(host='localhost', port=6379, db=0)

def on_connect(client, userdata, flags, rc):
    print("Connected")
    client.subscribe(sys.argv[3])

def on_message(client, userdata, message):
    print("Listenning: " + str(message.payload.decode()))
    r.set(message.topic + "-" + client._client_id.decode() + "-" + str(datetime.datetime.now()), message.payload.decode())
    
client = mqtt.Client(sys.argv[1])
client.on_connect = on_connect
client.on_message = on_message
client.connect(sys.argv[2])
client.loop_forever()
