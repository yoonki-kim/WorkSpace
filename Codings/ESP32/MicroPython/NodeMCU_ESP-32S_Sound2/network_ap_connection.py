import network
import machine

#wlan = WLAN(mode=WLAN.STA_IF)
wlan = network.WLAN(network.STA_IF)  #Create WLAN object

ssid = 'KT_GiGA_2G_99F3'
print("Network found!")
wlan.connect(ssid, auth=(4, 'axca1hf258'))
while not wlan.isconnected():
  machine.idle() # save power while waiting
  print('WLAN connection succeeded!')
  print('\nifconfig: {}\n'.format(wlan.ifconfig()))
  break


