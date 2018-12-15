
import network

#SSID = "dongbu4-3"                  #WiFi name 
#PASSWORD = "lightec43"            #WiFi password
#SSID = "Yoonki_iPhone"                  #WiFi name 
#PASSWORD = "iloveyoonki"            #WiFi password
SSID = 'KT_GiGA_2G_99F3'
PASSWORD = 'axca1hf258'

wlan = network.WLAN(network.STA_IF)  #Create WLAN object
wlan.active(True)                  #Activate the interface
wlan.scan()                        #Scan access point
wlan.isconnected()                 #Check whether the site is connected to the AP
wlan.connect(SSID, PASSWORD)       #Connect to AP
wlan.config('mac')                 #Get the MAC address of the interface
wlan.ifconfig()       

