import RPi.GPIO as gpio
import time

buzzer_pin = 16

gpio.setmode(gpio.BCM)
gpio.setup(buzzer_pin, gpio.OUT)

gpio.output(buzzer_pin, 1)
time.sleep(0.5)
gpio.output(buzzer_pin, 0)
time.sleep(0.5)

gpio.cleanup()
