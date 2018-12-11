# MicroPython on NodeMCU-ESP32S
# Inspired by http://www.raspberrypi-spy.co.uk/2015/03/bh1750fvi-i2c-digital-light-intensity-sensor/

import time

class BH1721():
    """ Implement BH1721 communication. """
    # Define some constants from the datasheet
    POWER_DOWN = 0x00 # No active state
    POWER_ON   = 0x01 # Power on
    
    # Switch measurement mode automatically by illuminance
    CONTINUOUS_AUTO_RES_MODE = 0x10  # 0x20 also
    # Start measurement at 1lx resolution. Time typically 120ms
    CONTINUOUS_HIGH_RES_MODE = 0x12  # 0x22 also
    # Start measurement at 8lx resolution. Time typically 16ms.
    CONTINUOUS_LOW_RES_MODE = 0x13  # 0x16, 0x23, 0x26 also

    res_mod = [(CONTINUOUS_AUTO_RES_MODE, "CONTINUOUS_AUTO_RES_MODE"),
               (CONTINUOUS_HIGH_RES_MODE, "CONTINUOUS_HIGH_RES_MODE"),
               (CONTINUOUS_LOW_RES_MODE, "CONTINUOUS_LOW_RES_MODE")]
    
    # addr=0x23 only
    def __init__(self, bus, addr=0x23):
        self.bus = bus
        self.addr = addr
        self.power_down()

    def _set_mode(self, mode):
        self.mode = mode
        self.bus.writeto(self.addr, bytes([self.mode]))

    def power_down(self):
        self._set_mode(self.POWER_DOWN)

    def power_on(self):
        self._set_mode(self.POWER_ON)

    def get_result(self, mode):
        """ Return current measurement result in lx. """   
        data = self.bus.readfrom(self.addr, 2)
        factor = 1.0
        return (data[0]<<8 | data[1]) / (1.2 * factor)

    def wait_for_result(self, mode):
        """ earlier measurements return previous reading """
        # 180ms wait in CONTINUOUS_AUTO_RES_MODE(0x10) and CONTINUOUS_HIGH_RES_MODE(0x12), else 24ms
        time.sleep_ms(180 if mode in (self.CONTINUOUS_AUTO_RES_MODE, self.CONTINUOUS_HIGH_RES_MODE) else 24)

    def do_measurement(self, mode):
        """Sample luminance (in lux), using specified sensor mode."""
        self._set_mode(mode)
        self.wait_for_result(mode)
        return self.get_result(mode)

def main():
    from machine import I2C, Pin
    #from bh1721 import BH1721
    #import time
    
    bus = I2C(scl=Pin(17),sda=Pin(16))
    sensor = BH1721(bus)

    while True:
        lux = sensor.do_measurement(BH1721.CONTINUOUS_AUTO_RES_MODE)
        print("%d lux" % lux)
        time.sleep(1)


if __name__=="__main__":
    main()
    





