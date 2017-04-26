#! /usr/bin/env python

import socket
import serial

UDP_IP = "192.168.3.197"
# UDP_IP = "127.0.0.1"
UDP_PORT = 6789

# ser = serial.Serial('/dev/tty.usbserial', 9600)
# ser.write(b'5')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
address = (UDP_IP, UDP_PORT)
sock.bind(address)


while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message:", data)