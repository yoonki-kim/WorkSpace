# connect/ show IP config a specific network interface
# see below for examples of specific drivers
import network
import utime

SSID = 'dongbu4-3'
PASSWORD = 'lightec43'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    wlan.connect(SSID, PASSWORD)
    print("Waiting for connection...")
    while not wlan.isconnected():
        utime.sleep(1)
print(wlan.ifconfig())

# now use usocket as usual
import usocket as socket
addr = socket.getaddrinfo('www.google.com', 80)[0][-1]
print('addr: ', addr)
s = socket.socket()
s.connect(addr)
s.send(b'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n')
data = s.recv(1000)
print(data)
s.close()
