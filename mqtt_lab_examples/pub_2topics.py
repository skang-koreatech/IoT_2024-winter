import paho.mqtt.client as mqtt
import random
import time

def on_connect(client, userdata, flags, rc, properties):
    print("Connected with result code " + str(rc))

pubClient = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
pubClient.on_connect = on_connect

pubClient.connect("test.mosquitto.org")
pubClient.loop_start()

try:
    while True:
        d = random.randrange(20, 36)
        temp = str(d)                
        print("temp", temp)
        
        h = random.randrange(20, 71, 10)
        humid = str(h)
        print("humidity", humid)        
        
        infot = pubClient.publish("125/room/temp/ksw", temp)
        infot.wait_for_publish()
        
        infot = pubClient.publish("125/room/humid/ksw", humid)
        infot.wait_for_publish()
        
        time.sleep(2)
except KeyboardInterrupt:
    print("Finished!")
    pubClient.loop_stop()
    pubClient.disconnect()

