from machine import I2C, Pin
from bh1750 import BH1750
import time

bus = I2C(scl=Pin(17),sda=Pin(16))
sensor = BH1750(bus)

while True:
    for mode, name  in BH1750.res_mod:
        #print(mode, name)
        lux = sensor.do_measurement(mode)
        print("mode : %-30s, lux: %d" % (name, lux))
    print("\n")
    time.sleep(1)

