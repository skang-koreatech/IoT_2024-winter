import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc, properties):
    print("connected with result code " + str(rc))
    subClient.subscribe("125/room/temp/ksw") 
    subClient.subscribe("125/room/humid/ksw")
        
def on_message(client, userdata, msg):
    print("Topic: " + msg.topic + " Message: " + msg.payload.decode("utf-8"))
    
    if msg.topic == "125/room/temp/ksw":    
        temp = int(msg.payload.decode("utf-8"))
        
        if temp >= 20 and temp < 25:
            print("Moderate temperature")
        elif temp >= 25 and temp <30:
            print("High temperature")
        else:
            print("Very high temperature")
      
    elif msg.topic == "125/room/humid/ksw":
        humid = int(msg.payload.decode("utf-8"))
        
        if humid >=20 and humid < 30:
            print("Low humidity")
        elif humid >= 30 and humid < 50:
            print("Mid humidity")
        else:
            print("High humidity")
    else:
        print("Error")

subClient = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
subClient.on_connect = on_connect
subClient.on_message = on_message
subClient.connect("test.mosquitto.org")


try:
    subClient.loop_forever()
except KeyboardInterrupt:
    print("Finished!")
    subClient.unsubscribe("125/room/temp/ksw") 
    subClient.unsubscribe("125/room/humid/ksw") 
    subClient.disconnect()

