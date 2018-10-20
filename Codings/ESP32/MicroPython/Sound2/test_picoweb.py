# web server using picoweb on micropython
import picoweb
import network

app = picoweb.WebApp(__name__)

wlan = network.WLAN(network.STA_IF)
if wlan.active():
    STA_addr = wlan.ifconfig()[0]
else:
    print("settng up wifi network first!")

@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Hello world from picoweb running on the ESP32")

app.run(debug=True, host = STA_addr)
