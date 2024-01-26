import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
import sys
import time
from time import sleep     # Import the sleep from time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

runTime = 20
if (len(sys.argv) > 1):
   runTime = int(sys.argv[1])

pin1 = 13
pin2 = 11

GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)   
GPIO.setup(pin2, GPIO.IN) # sets pin as input

t0 = time.time()
while  (time.time() < t0+runTime): 
   if GPIO.input(pin2):
      GPIO.output(pin1,GPIO.HIGH)
   if not(GPIO.input(pin2)):
      GPIO.output(pin1,GPIO.LOW)
GPIO.cleanup()
