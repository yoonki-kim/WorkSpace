
from machine import Pin, PWM
import time, math

p22 = Pin(12)
pwm1 = PWM(p22, freq=1000, duty=0)  #freq:Hz, range of duty:0~1023

value = []

def pulse(pin, interval):   #interval:ms
    for i in range(20):
        var = (int(math.sin(i/10*math.pi)*500+500))
        #print(var)
        value.append(var)
        pin.duty(var)
        time.sleep_ms(interval)
    print(value)

pulse(pwm1, 50)
