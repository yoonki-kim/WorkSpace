#ADC & DAC basic
from pin_map import *
from machine import ADC, DAC
import time

dac = DAC(GPIO25)
dac.write(0.5)
print("DAC output activating...")

adc = ADC()
apin = adc.channel(pin=GPIO39, attn=ADC.ATTN_11DB)
#ADC.ATTN_0DB : x1.00
#ADC.ATTN_5DB : x1.78
#ADC.ATTN_6DB : x2.00
#ADC.ATTN_11DB : x3.55

for i in range(10):
    val = apin.value()
    volt = apin.voltage()
    print("ADC input value : %d, %d[mV]" % (val,volt))
    time.sleep(1)
