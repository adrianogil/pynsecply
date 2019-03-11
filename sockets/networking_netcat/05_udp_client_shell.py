import socket
import sys

HOST = '127.0.0.1'
PORT = 9000
DATA = 'AAAAAAAAAA'

if len(sys.argv) >= 2:
    HOST = sys.argv[1]

if len(sys.argv) >= 3:
    PORT = int(sys.argv[2])

if len(sys.argv) >= 4:
    DATA = sys.argv[3]

def udp_client():
    client = socket.socket( socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(DATA, ( HOST, PORT ))
    data, addr = client.recvfrom(4096)
    print "From: " + addr
    print data

if __name__ == '__main__':
    udp_client()