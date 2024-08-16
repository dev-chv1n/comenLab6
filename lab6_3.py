import RPi.GPIO as GPIO
import time
LED = 3
SW = 17
count = 0
ledState = True
GPIO.setmode(GPIO.BCM)
#GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
#GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        if GPIO.wait_for_edge(SW, GPIO.FALLING):
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
