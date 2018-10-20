from mqtt_simple import MQTTClient
from machine import Pin
import machine
from network import WLAN
import time

#wifi setting
#SSID = "SK_WiFi0EFD" #insert your wifi ssid
#PASSWORD = "1501051742" #insert your wifi password

SSID = "DBLIGHTEC4-5" #insert your wifi ssid
PASSWORD = "lightec45" #insert your wifi password

#SSID = "Yoonki's iPhone" #insert your wifi ssid
#PASSWORD = "yoonki-love" #insert your wifi password

#SSID = "KT_GiGA_2G_99F3" #insert your wifi ssid
#PASSWORD = "axca1hf258" #insert your wifi password

MQTT_SERVER = "mqtt.mydevices.com"
MQTT_USERNAME = "12abdb90-bf6e-11e7-b71a-77dc3dda8745" #insert your MQTT username
MQTT_PASSWORD = "3d79db74637272c4807efd00e57f8414babd25b9" #insert your MQTT
#CLIENT_ID = "c18b4a20-bf8b-11e7-993a-9b80361bb997" #insert your client ID (test_LumiSmart)
#CLIENT_ID = "8ec83ee0-1e13-11e8-96c3-51e4789cd606" #insert your client ID (ESP8266)
CLIENT_ID = "bf021390-1e88-11e8-9f38-9fae3d42ebf0" #insert your client ID (ESP32)
#CLIENT_ID = "3b95cd40-23eb-11e8-ab82-a3edb533e078" #insert your client ID (Device919d)

TOPIC = ("v1/%s/things/%s/data/1" % (MQTT_USERNAME, CLIENT_ID))

def sub_cb(topic, msg):
    print(msg)

def connectWifi(ssid,passwd):
    #print("ssid, password : ", ssid, passwd)
    global wlan
    wlan=WLAN(mode=WLAN.STA)
    #wlan.connect(ssid, auth=(WLAN.WPA2, passwd), timeout=5000)
    wlan.connect(ssid, auth=(WLAN.WPA2, passwd), timeout=5000)
    while not wlan.isconnected():
        machine.idle()  #save power while waiting
    print("WiFi connection succeeded!")
    time.sleep(1)
    print(wlan.ifconfig())

connectWifi(SSID, PASSWORD)

#print("\n wlan.ifconfig : ", wlan.ifconfig())
#c = MQTTClient(CLIENT_ID, MQTT_SERVER, 0, MQTT_USERNAME, MQTT_PASSWORD)
c = MQTTClient(CLIENT_ID, MQTT_SERVER, user=MQTT_USERNAME, password=MQTT_PASSWORD, port=1883)
print("\n ssl, user, password : ", c.ssl, c.user, c.pswd)

c.set_callback(sub_cb)
print("\n debug break point #1")

c.connect()
print("\n debug break point #2")

temp = 0

def senddata():
    global temp
    temp = temp + 1 # sample data
    print("temp : ", temp)
    c.publish(TOPIC, str(temp))

    #time.sleep(2)
    print("temperature is: ", temp)
    print("data sent")

while True:
    try:
        senddata()
        time.sleep(2)
    except OSError:
        pass
