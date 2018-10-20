from network import WLAN
import machine

wlan = WLAN(mode=WLAN.STA)

# Home
my_ssid = 'KT_GiGA_2G_99F3'
my_password = 'axca1hf258'

# DropTop Cafe Internet
#my_ssid = 'DROPTOP 2.4GHz'
#my_password = 'A1234567890'

def startftp():
    nets = wlan.scan()
    for net in nets:
        if net.ssid == my_ssid:
            print("Network found!")
            wlan.connect(net.ssid, auth=(net.sec, my_password), timeout=5000)
            while not wlan.isconnected():
                machine.idle() # save power while waiting
            print('WLAN connection succeeded!')
            print('\nifconfig: {}\n'.format(wlan.ifconfig()))
            break

if __name__ == "__main__":
#    from ftp_server import *
    
    startftp()
