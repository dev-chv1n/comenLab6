import RPi.GPIO as GPIO
import time

SW1 = 11
SW2 = 13
lcd_position =0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SW1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down = GPIO.PUD_UP)

GPIO.add_event_detect(SW1, GPIO.FALLING)
GPIO.add_event_detect(SW2, GPIO.FALLING)

try:
    while True:
        if GPIO.event_detected(SW1):
            lcd_position +=1
            print(f"SW1 Pressed : {lcd_position}")
        elif GPIO.event_detected(SW2):
            lcd_position -=1
            print(f"SW2 Pressed : {lcd_position}")

        time.sleep(0.3)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\n BYE...")
