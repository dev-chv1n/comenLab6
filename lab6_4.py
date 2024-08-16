import RPi.GPIO as GPIO
import time
RED = 2
GREEN = 3
BLUE = 4

SW = 17
count = 0
ledState = True
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)


def black():
    if count == 1:

        GPIO.output(RED,0)
        GPIO.output(GREEN,0)
        GPIO.output(BLUE,0)
def blue():
    if count == 2:

        GPIO.output(RED,0)
        GPIO.output(GREEN,0)
        GPIO.output(BLUE,1)
def green():
    if count == 3:

        GPIO.output(RED,0)
        GPIO.output(GREEN,1)
        GPIO.output(BLUE,0)
def cyan():
    if count == 4:

        GPIO.output(RED,0)
        GPIO.output(GREEN,1)
        GPIO.output(BLUE,1)
def red():
    if count == 5:

        GPIO.output(RED,1)
        GPIO.output(GREEN,0)
        GPIO.output(BLUE,0)
def magenta():
    if count == 6:

        GPIO.output(RED,1)
        GPIO.output(GREEN,0)
        GPIO.output(BLUE,1)
def yellow():
    if count == 7:

        GPIO.output(RED,1)
        GPIO.output(GREEN,1)
        GPIO.output(BLUE,0)
def white():
    if count == 8:

        GPIO.output(RED,1)
        GPIO.output(GREEN,1)
        GPIO.output(BLUE,1)


try:
    while True:
        if GPIO.wait_for_edge(SW, GPIO.FALLING):
            count += 1
            black();
            blue();
            green();
            cyan();
            red();
            magenta();
            yellow();
            white();         
        if count == 8 :
            count = 0

except KeyboardInterrupt:
    GPIO.cleanup();
print("\nbye!")