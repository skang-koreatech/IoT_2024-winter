import RPi.GPIO as gpio
import time

switch_pin = 12

gpio.setmode(gpio.BCM)
gpio.setup(switch_pin, gpio.IN, gpio.PUD_UP)

try:
    while True:
        if gpio.input(switch_pin) == 0:
            print("Switch On")
            time.sleep(0.5)
        else:
            print("Switch Off")
            time.sleep(0.5)
except KeyboardInterrupt:
    gpio.cleanup()
    

