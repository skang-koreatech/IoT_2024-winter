import paho.mqtt.client as mqtt
import random
import time

def on_connect(client, userdata, flags, rc, properties):
    print("Connected with result code " + str(rc))

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect

mqttc.connect("test.mosquitto.org")
mqttc.loop_start()

try:
    while True:
        d = random.randrange(20, 36)
        msg = str(d)                
        print("temp", msg)
        
        infot = mqttc.publish("room1/temp", msg)
        infot.wait_for_publish()
        
        time.sleep(1)
except KeyboardInterrupt:
    print("Finished!")
    mqttc.loop_stop()
    mqttc.disconnect()

