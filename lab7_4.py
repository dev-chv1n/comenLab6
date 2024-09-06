import RPi.GPIO as GPIO
import time
import drivers
from time import sleep
display = drivers.Lcd()
display.lcd_clear()

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
            if lcd_position == 1:
                display.lcd_clear()
                display.lcd_display_string("NATAPONG",1) 
                display.lcd_display_string("116630462041-0",2)
            elif lcd_position == 2:
                display.lcd_clear()
                display.lcd_display_string("KITTIPOOM",1) 
                display.lcd_display_string("116630462018-8",2)
            elif lcd_position == 3:
                display.lcd_clear()
                display.lcd_display_string("PORPEANG",1) 
                display.lcd_display_string("116630462038-6",2)
                lcd_position = 0
        elif GPIO.event_detected(SW2):
            display.lcd_clear()
            display.lcd_display_string("BYE!!!",1) 
            sleep(5)
            display.lcd_clear()
            exit()

        time.sleep(0.3)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\n BYE...")
