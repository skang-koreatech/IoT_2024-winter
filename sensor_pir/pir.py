import RPi.GPIO as gpio
import time

pir_pin = 21

gpio.setmode(gpio.BCM)
gpio.setup(pir_pin, gpio.IN)

try:
    while True:    
        pir_in = gpio.input(pir_pin)
        
        if pir_in == True:
            print("Detected")
            time.sleep(0.5)
        else:
            print("Not detected")
            time.sleep(0.5)
            
except KeyboardInterrupt:
    gpio.cleanup()
