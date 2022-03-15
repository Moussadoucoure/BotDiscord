import RPi.GPIO as GPIO
import time

class Raspi(object):
    def __init__(self):
        print("Instance Raspi Créée!")

    def blink (self):
        print("Disco party!")

        led = 13
        GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering
        GPIO.setup(led, GPIO.OUT)

        for i in range (100):
            GPIO.output(led,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(led,GPIO.LOW)
            time.sleep(0.1)

        GPIO.cleanup() # Reinitialise les pins    
