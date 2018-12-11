import network

SSID = 'dongbu4-3'
PASSWORD = 'lightec43'

ap = network.WLAN(network.AP_IF) # create access-point interface
ap.active(True)         # activate the interface
ap.config(essid='ESP-AP') # set the ESSID of the access point


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        pass
print('network config:', wlan.ifconfig())
