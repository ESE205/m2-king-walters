# Imports
import time
from time import sleep
import sys
import RPi.GPIO as  GPIO

# Blinkrate and Runtime
blinkRate = 1
if (len(sys.argv) > 1):
   blinkRate = int(sys.argv[1])
runTime = 100
if (len(sys.argv) > 2):
   runTime = int(sys.argv[2])

# Debug
DEBUG = False
if "-debug" in sys.argv:
   DEBUG = True

# GPIO Setup
LED_pin = 13
switch_pin = 11
LED_ON = False
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(switch_pin, GPIO.IN)

# Read to file 
with open("data.txt", "w") as f:

   # Blink LED
   t0 = time.time()
   loopCount = 1
   while (time.time() < t0+runTime):
      if (GPIO.input(switch_pin)):
         LED_ON = not(LED_ON)
         GPIO.output(LED_pin,LED_ON)
         f.write(f"{time.time():.0f}\t{LED_ON}\n")
         if DEBUG:
            print(f"{time.time():.0f}\t{loopCount}\t{LED_ON}\n")
         loopCount = loopCount + 1
         sleep(blinkRate)

# Cleanup
GPIO.cleanup()


