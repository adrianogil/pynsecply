#!/usr/bin/python

import socket

ip = raw_input("Enter target IP:\n")
for porta in range(1,65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if s.connect_ex((ip,porta)) == 0:
        print porta, "OPEN"
    s.close()