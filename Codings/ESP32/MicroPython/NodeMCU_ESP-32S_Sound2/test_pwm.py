from machine import PWM, Pin
import time

PWM_PORT = 2
PWM_FREQ = 1000
DUTY_DEFAULT = 1023
DUTY_MIN = 0
DUTY_MAX = 1023

pwm = PWM(Pin(PWM_PORT), freq=PWM_FREQ, duty=DUTY_DEFAULT)

for i in range(1023):
  pwm.duty(1023-i)
  print("duty: {}".format(1023-i))
  time.sleep_ms(10)
