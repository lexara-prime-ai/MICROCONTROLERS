# import time
# from machine import Pin
# 
# led = Pin("LED",Pin.OUT)
# 
# while True:
#     led.toggle()
#     time.sleep_ms(500)

# led.toggle()

import network
import time
nic = network.Driver(...)
if not nic.isconneted():
    nic.connect()
    print("Waiting for connection...")
    while not nic.isconnected():
        time.sleep(1)

print(nic.ifconfig())

import socket
addr = socket.getaddrinfo('micropython.org', 80)[0][-1]
s = socket.socket()
                                                 
s.connect(addr)
s.send(b'GET / HTTP/1.1\r\nHost: micropython.org\r\n\r\n')

data = s.recv(1000)
s.close()
                                                 