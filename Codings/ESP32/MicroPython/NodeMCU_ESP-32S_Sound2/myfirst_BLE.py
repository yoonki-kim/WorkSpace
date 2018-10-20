from pin_map import *

from network import Bluetooth
import time
from machine import Timer
from machine import Pin
from blinky import Blink

led2 = Pin(GPIO2, mode=Pin.OUT)
blink_led = Blink(led2, interval=0.5)
blink_led.start()

bluetooth =Bluetooth()
bluetooth.set_advertisement(name='LumiSmart', manufacturer_data='yoonki', service_data='kim', service_uuid=0x3550)

def conn_cb(bt_o):
    events = bt_o.events()
    if events & Bluetooth.CLIENT_CONNECTED:
        print("Client connected")
        blink_led.stop()
        led2.value(1)
    elif events & Bluetooth.CLIENT_DISCONNECTED:
        print("Client disconnected")
        blink_led.start()

bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)

bluetooth.advertise(True)

srv1 = bluetooth.service(uuid=0x4248, isprimary=True)
chr1 = srv1.characteristic(uuid=0x0427, value=25)

char1_read_counter = 0
def char1_cb_handler(chr):
    global char1_read_counter
    char1_read_counter += 1
    #print("chr: ", chr)

    events = chr.events()
    if events & Bluetooth.CHAR_WRITE_EVENT:
        print("Write request with value = {}".format(chr.value()))
    else:
        if char1_read_counter < 3:
            print("Read request on char 1")
        else:
            return 'ABC DEF'

char1_cb = chr1.callback(trigger=Bluetooth.CHAR_WRITE_EVENT | Bluetooth.CHAR_READ_EVENT, handler=char1_cb_handler)

srv2 = bluetooth.service(uuid=1234, isprimary=True) #1234=0x04D2
chr2 = srv2.characteristic(uuid=4567, value=0x1234) #4567=0x11D7, 0x1234=4660

char2_read_counter = 0xF0 #240
def char2_cb_handler(chr):
    global char2_read_counter
    char2_read_counter += 1

    if char2_read_counter > 0xF1: #241
        return char2_read_counter

char2_cb = chr2.callback(trigger=Bluetooth.CHAR_READ_EVENT, handler=char2_cb_handler)
