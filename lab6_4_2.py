import RPi.GPIO as GPIO
import time
RED = 40
GREEN = 38
BLUE = 36

SW = 13
pressCount = 0
redLedState = True
greenLedState = True
blueLedState = True

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

try:
    while True:
        if GPIO.wait_for_edge(SW, GPIO.RISING):
            pressCount += 1
            print("presscount = " , pressCount)
            print(f"redLedState: {redLedState}  greenLedState: {greenLedState}  blueLedState: {blueLedState}")
            GPIO.output(RED,redLedState)
            if pressCount % 4 == 0:
                redLedState = not redLedState
                
            GPIO.output(GREEN,greenLedState)
            if pressCount % 2 == 0:
                greenLedState = not greenLedState
                
            GPIO.output(BLUE,blueLedState)
            if pressCount % 1 == 0 :
                blueLedState = not blueLedState


except KeyboardInterrupt:
    GPIO.cleanup();
print("\nbye!")