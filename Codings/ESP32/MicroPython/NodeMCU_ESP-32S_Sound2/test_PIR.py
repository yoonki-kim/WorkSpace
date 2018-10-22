from machine import ADC, Pin
import time

adc = ADC(Pin(36))

while True:
    x = adc.read()
    print("{0}".format(x))
    time.sleep_ms(100)
    
