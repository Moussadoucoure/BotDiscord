import RPi.GPIO as GPIO
import time
pwmLed1 = 26 # pulse width modulation
led2 = 13
btnPin = 2

GPIO.setwarnings(False)

# Pin setup:
GPIO.setmode(GPIO.BCM) # Broadcom numero-pin
GPIO.setup(pwmLed1,GPIO.OUT)
pwm = GPIO.PWM(pwmLed1, 10) # initialise la led a  X hertz par seconde
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # btnPIN setup avec pull-up envoie de signall

# Setup initial :
GPIO.output(led2, GPIO.LOW)
pwm.start(50)

try:
  while True:
      if GPIO.input(btnPin): # Bouton relaché
          pwm.ChangeDutyCycle(0)
      else:
          pwm.ChangeDutyCycle(50)    

      GPIO.output(led2, GPIO.HIGH)
      time.sleep(0.1)
      GPIO.output(led2, GPIO.LOW)
      time.sleep(0.1)
except KeyboardInterrupt: # si CTRL+C, exit
  pwm.stop()
  GPIO.cleanup() # Reinitialise les pins