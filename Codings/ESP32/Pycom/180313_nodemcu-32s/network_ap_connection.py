from network import WLAN
import machine

wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()
for net in nets:
    if net.ssid == 'KT_GiGA_2G_99F3':
        print("Network found!")
        wlan.connect(net.ssid, auth=(net.sec, 'axca1hf258'), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        print('\nifconfig: {}\n'.format(wlan.ifconfig()))
        break
