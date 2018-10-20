import pin_map
from machine import Pin
import time

led = Pin(pin_map.GPIO2, mode = Pin.OUT)
while (1):
  led.toggle()
  time.sleep(0.5)
