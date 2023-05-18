import RPi.GPIO as gpio
import os
import time

"""
Using a simple button to switch on/off.
Connect one button "terminal" (both sides) with GPIO pin 27, the other one with GND next to it.
Button has to be longpressed.
"""

PIN = 27
gpio.setmode(gpio.BCM)
gpio.setup(PIN, gpio.IN)

while True:
    if gpio.input(PIN) == gpio.LOW:
        time.sleep(0.75)
        if gpio.input(PIN) is gpio.LOW:
            os.system("shutdown now-h")
            time.sleep(1)
