import RPi.GPIO as GPIO
import time
LED = 11
SW = 13
count = 0
ledState = True
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        if GPIO.wait_for_edge(SW, GPIO.RISING):
            if ledState == True:
                GPIO.output(LED, ledState)
                ledState = 0
                print("LED ON")
            else :
                GPIO.output(LED, ledState)
                ledState = 1
                print("LED OFF")
except KeyboardInterrupt:
    GPIO.cleanup();
print("\nbye!")
