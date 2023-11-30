import network
import secrets
import time
from machine import Pin

indicator = Pin("LED",Pin.OUT)

wlan = network.WLAN(network.STA_IF)
print(f'{wlan}')
wlan.active(True)

wlan.connect(secrets.SSID, secrets.PASSWORD)

if wlan.isconnected():
    print(f'Connected: {wlan.isconnected()}')
    while wlan.isconnected():
        indicator.toggle()
        time.sleep_ms(1000)')')
