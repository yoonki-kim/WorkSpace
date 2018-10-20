#ADC Calibration
from pin_map import *
from machine import ADC, DAC
import time

adc = ADC()

# Output 1100mV Vref of GPIO25 (DAC1) (P22)
adc.vref_to_pin(GPIO25) #DAC1
print("From now on, Vref(1100mV) output on GPIO25 for 10sec.")
print("Measure Vref with most accurate Voltmeter you have.")
for i in range(3):
    time.sleep(1)
    print("elapsed %d[sec] ..." % (i+1))

# Measure Vref with most accurate Voltmeter
# Note down the reading in millivolts, eg. 1113[mV]
#measured_val = 1113
#print("measured_val : %d" % measured_val)

# Set Calibration
#adc.vref(measured_val) #see note above
#time.sleep(2)

# Reset NodeMCU-32S Module

# Check calibration by reading a known voltage
adc_c = adc.channel(pin=GPIO39, attn=ADC.ATTN_11DB)

# Again Output 1100mV Vref of GPIO25 (DAC1) (P22)

#print("Again Output %d mV of GPIO25" % (measured_val))
#time.sleep(1)

for i in range(5):
    print("Calibrate Value reading : %d " % adc_c.value())
    print("Calibrate Voltage reading : %d [mV]" % adc_c.voltage())
#time.sleep(10)
