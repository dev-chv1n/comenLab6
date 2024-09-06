import drivers
from time import sleep
display = drivers.Lcd()
display.lcd_clear()

try:
    while True:
        print("Writing to LCD!!")
        display.lcd_display_string("LAB7_LCD",1) 
        display.lcd_display_string("HELLO WORLD",2)
        sleep(2)

        display.lcd_display_string("IM ENGINEER",1)
        display.lcd_display_string("123456798abcdef",2)
        sleep(2)
        
        display.lcd_clear()
        sleep(2)

except KeyboardInterrupt:
    display.lcd_clear()
    print("\nbye...")
        
        
        