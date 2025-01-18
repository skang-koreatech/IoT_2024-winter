import paho.mqtt.client as mqtt

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

mqttc.connect("test.mosquitto.org")

mqttc.loop_start()

infot = mqttc.publish("hello/world", "Hello")
infot.wait_for_publish()

mqttc.loop_stop()
mqttc.disconnect()
