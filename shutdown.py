import RPi.GPIO as gpio
import os
import time

"""
Using a simple button to start the shutdown process of the Raspberry Pi.
The goal is to give the user a chance to avoid hard resetting the Raspi every time.
"""

PIN = 27
gpio.setmode(gpio.BCM)
gpio.setup(PIN, gpio.IN, gpio.PUD_UP)

while True:
    time.sleep(0.5)
    if gpio.input(PIN) == gpio.LOW:
        time.sleep(0.5) # the button needs to be long-pressed to confirm the shutdown
        if gpio.input(PIN) is gpio.LOW:
            os.system("shutdown now -h")
