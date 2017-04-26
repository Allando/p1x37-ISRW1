#! /usr/bin/env python

import socket
import serial

UDP_IP = "192.168.3.250"
UDP_PORT = 6789
address = (UDP_IP, UDP_PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("",UDP_PORT))

# ser = serial.Serial('/dev/tty.usbserial', 9600)
# ser.write(b'5')

while True:
    data, addr = server.recvfrom(1024) # buffer size is 1024 bytes
    print("received message:", data)