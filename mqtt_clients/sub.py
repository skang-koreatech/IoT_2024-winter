import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc, properties):
    print("connected with result code " + str(rc))
    client.subscribe("room1/temp")
        
def on_message(client, userdata, msg):
    print("Topic: " + msg.topic + " Message: " + msg.payload.decode("utf-8"))

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org")

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Finished!")
    client.unsubscribe("room1/temp")
    client.disconnect()

