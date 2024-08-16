import RPi.GPIO as GPIO
import time
RED = 2
GREEN = 3
BLUE = 4

SW = 17
pressCount = 0
bool redLedState = 0
bool greenLedState = 0
bool blueLedState = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        if GPIO.wait_for_edge(SW, GPIO.FALLING):
            pressCount += 1
            GPIO.output(RED,redLedState)
            if pressCount % 4:
                redLedState != redLedState
                
            GPIO.output(GRREEN,greenLedState)
            if pressCount % 2:
                greenLedState != greenLedState
                
            GPIO.output(GRREEN,blueLedState)
            if pressCount % 1:
                blueLedState != blueLedState


except KeyboardInterrupt:
    GPIO.cleanup();
print("\nbye!")