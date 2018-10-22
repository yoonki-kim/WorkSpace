# MicroPython on NodeMCU-ESP32S
# Inspired by http://www.raspberrypi-spy.co.uk/2015/03/bh1750fvi-i2c-digital-light-intensity-sensor/

import time

class BH1750():
    """ Implement BH1750 communication. """
    # Define some constants from the datasheet
    POWER_DOWN = 0x00 # No active state
    POWER_ON   = 0x01 # Power on
    RESET      = 0x07 # Reset data register value
    
    # Start measurement at 1lx resolution. Time typically 120ms
    CONTINUOUS_HIGH_RES_MODE_1 = 0x10
    # Start measurement at 0.5lx resolution. Time typically 120ms
    CONTINUOUS_HIGH_RES_MODE_2 = 0x11
    # Start measurement at 4lx resolution. Time typically 16ms.
    CONTINUOUS_LOW_RES_MODE = 0x13

    # Start measurement at 1lx resolution. Time typically 120ms
    # Device is automatically set to Power Down after measurement.
    ONE_TIME_HIGH_RES_MODE_1 = 0x20
    # Start measurement at 0.5lx resolution. Time typically 120ms
    # Device is automatically set to Power Down after measurement.
    ONE_TIME_HIGH_RES_MODE_2 = 0x21
    # Start measurement at 4lx resolution. Time typically 16ms
    # Device is automatically set to Power Down after measurement.
    ONE_TIME_LOW_RES_MODE = 0x23
    
    res_mod = [(CONTINUOUS_HIGH_RES_MODE_1, "CONTINUOUS_HIGH_RES_MODE_1"),
               (CONTINUOUS_HIGH_RES_MODE_2, "CONTINUOUS_HIGH_RES_MODE_2"),
               (CONTINUOUS_LOW_RES_MODE, "CONTINUOUS_LOW_RES_MODE"),
               (ONE_TIME_HIGH_RES_MODE_1, "ONE_TIME_HIGH_RES_MODE_1"),
               (ONE_TIME_HIGH_RES_MODE_2, "ONE_TIME_HIGH_RES_MODE_2"),
               (ONE_TIME_LOW_RES_MODE, "ONE_TIME_LOW_RES_MODE")]
    
    # default addr=0x23 if addr pin floating or pulled to ground
    # addr=0x5c if addr pin pulled high
    def __init__(self, bus, addr=0x23):
        self.bus = bus
        self.addr = addr
        self.power_down()
        self.reset()

    def _set_mode(self, mode):
        self.mode = mode
        self.bus.writeto(self.addr, bytes([self.mode]))

    def power_down(self):
        self._set_mode(self.POWER_DOWN)

    def power_on(self):
        self._set_mode(self.POWER_ON)

    def reset(self):
        self.power_on() #It has to be powered on before resetting
        self._set_mode(self.RESET)

    def get_result(self, mode):
        """ Return current measurement result in lx. """   
        data = self.bus.readfrom(self.addr, 2)
        # 2.0x in High Resolution Mode2, else 1.0x
        factor = 2.0 if mode in (0x11, 0x21) else 1.0
        return (data[0]<<8 | data[1]) / (1.2 * factor)

    def wait_for_result(self, mode):
        """ earlier measurements return previous reading """
        # 24ms wait in Low Resolution mode, else 180ms
        time.sleep_ms(24 if mode in (0x13, 0x23) else 180)

    def do_measurement(self, mode):
        """Sample luminance (in lux), using specified sensor mode."""
        # continuous modes
        if mode & 0x10 and mode != self.mode:
            self._set_mode(mode)
        # one shot modes
        if mode & 0x20:
            self._set_mode(mode)
        
        self.wait_for_result(mode)
        
        return self.get_result(mode)

def main():
    from machine import I2C, Pin
    #from bh1750 import BH1750
    #import time
    
    bus = I2C(scl=Pin(17),sda=Pin(16))
    sensor = BH1750(bus)

    while True:
        lux = sensor.do_measurement(BH1750.ONE_TIME_HIGH_RES_MODE_1)
        print("%d lux" % lux)
        time.sleep(1)


if __name__=="__main__":
    main()
    




