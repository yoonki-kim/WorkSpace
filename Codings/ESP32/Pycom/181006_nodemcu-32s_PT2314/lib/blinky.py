# blink class by yoonki.kim, 2018-07-17
from pin_map import *
from machine import Pin, Timer

class Blink:

    def __init__(self, pin, interval=0.5):
        self.pin = pin
        self.interval = interval

    def start(self):
        #self.count = 0
        self.timer = Timer.Alarm(self.timer_callback, self.interval, periodic=True)

    def timer_callback(self, timer):
        self.pin.toggle()
        #self.count += 1
        #print("#blink count : ", self.count)

    def stop(self):
        self.timer.cancel()

if __name__ == "__main__":
#from blinky import Blink
#from machine import Pin
    led2 = Pin(GPIO2, mode=Pin.OUT)
    blink_led = Blink(led2, interval=0.5)
    blink_led.start()
