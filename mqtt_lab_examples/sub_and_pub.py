import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("connected with result code " + str(rc))
    client.subscribe("125/room/temp/ksw")
        
def on_message(client, userdata, msg):
    print("Topic: " + msg.topic + " Message: " + msg.payload.decode("utf-8"))
    
    temp = int(msg.payload.decode("utf-8"))
    
    if temp >= 22 and temp < 27:
        print("기온 보통")
    elif temp >= 27:
        print("기온 높음")
        
        infot = pubClient.publish("125/room/aircon/ksw", "on")
        infot.wait_for_publish()
    else:
        print("기온 낮음")
        
        infot = pubClient.publish("125/room/aircon/ksw", "off")
        infot.wait_for_publish()   

subClient = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
subClient.on_connect = on_connect
subClient.on_message = on_message
subClient.connect("test.mosquitto.org")

pubClient = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
pubClient.connect("test.mosquitto.org")
pubClient.loop_start()

try:
    subClient.loop_forever()
except KeyboardInterrupt:
    print("Finished!")
    subClient.unsubscribe("125/room/temp/ksw") 
    subClient.disconnect()
    pubClient.loop_stop()
    pubClient.disconnect()

