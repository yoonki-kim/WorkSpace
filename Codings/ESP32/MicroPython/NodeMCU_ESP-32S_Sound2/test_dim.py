# MicroPython 
from machine import PWM, Pin
import time

PWM_PORT = 2  # Pin(2) is on-board led
PWM_FREQ = 1000

DUTY_DEFAULT = 1023
DUTY_MIN = 0
DUTY_MAX = 1023

DIM_STOP = 0x00
DIM_UP = 0x01
DIM_DOWN = 0x02

direction = DIM_DOWN
bright = 100    # brightness : 0~100%

def cal_bright_to_duty(bright):
  duty = (DUTY_MAX/100)*bright
  return int(duty)

pwm = PWM(Pin(PWM_PORT), freq=PWM_FREQ, duty=DUTY_DEFAULT)

while(True):
  #global bright, direction
  if direction == DIM_DOWN:
    print("Dim Down..., bright: %d " % (bright,))
    bright -= 2
    if bright <= 0:    # Keep Brightness at or below 100%
      bright = 0
      print("You are at Full Bright")
      direction = DIM_UP
    duty = cal_bright_to_duty(bright)
    pwm.duty(duty)
    time.sleep_ms(25)
    print("New duty: %d, bright: %d " % (duty, bright))
  if direction == DIM_UP:
    print("Dim Up..., bright: %d " % (bright,))
    bright += 2
    if bright >= 100:    # Keep Brightness at or below 100%
      bright = 100
      print("You are at Full Bright")
      direction = DIM_DOWN
    duty = cal_bright_to_duty(bright)
    pwm.duty(duty)
    time.sleep_ms(25)
    print("New duty: %d, bright: %d " % (duty, bright))
  if direction == DIM_STOP:
    print("Dim Stop!")
    time.sleep_ms(25)
