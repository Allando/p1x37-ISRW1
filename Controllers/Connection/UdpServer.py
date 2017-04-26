#! /usr/bin/env python

import socket
import serial

UDP_PORT = 6789

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("", UDP_PORT))

# ser = serial.Serial('/dev/tty.usbserial', 9600)
# ser.write(b'5')

while True:
    data, addr = server.recvfrom(1024) # buffer size is 1024 bytes
    print("received message:", data)