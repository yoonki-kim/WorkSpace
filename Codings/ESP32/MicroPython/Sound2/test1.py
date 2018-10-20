# blink class by yoonki.kim, 2018-07-17

from pin_map import *
from machine import Pin, Timer
from blinky import Blink
import time

led2 = Pin(GPIO2, mode=Pin.OUT)
blink_500ms = Blink(led2, 1)

time.sleep(2)
print("2sec delay")

blink_500ms.start()
time.sleep(5)
print("5sec delay")

blink_500ms.stop()
