import network

def connect():
    # Home
    my_ssid = 'KT_GiGA_2G_99F3'
    my_password = 'axca1hf258'

    # DropTop Cafe Internet
    #my_ssid = 'DROPTOP 2.4GHz'
    #my_password = 'A1234567890'

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(my_ssid, my_password)   #Connect to AP
        i = 0
        while not wlan.isconnected():
            i = i + 1
            print("%d times trying to connect..." % i)
            if (i > 6):
                print("No AP found! Try again next.")
                wlan.disconnect()
                break
    print('network config:', wlan.ifconfig())

if __name__ == "__main__":
    connect()
