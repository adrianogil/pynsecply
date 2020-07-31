#!/usr/bin/python
import socket
import sys


if len(sys.argv) == 1:
    ip = input("Enter target IP:\n")
else:
    ip = sys.argv[1]

print("Using IP: %s" % (ip,))

open_ports = []

for port in range(1, 65535):
    print("[debug] Testing port %s" % (port,))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if s.connect_ex((ip, port)) == 0:
        open_ports.append(port)
    s.close()

print("The following ports are open:")
for port in open_ports:
    print("%s" % (port,))
