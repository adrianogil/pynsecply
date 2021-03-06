# https://pymotw.com/2/socket/tcp.html
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 11111)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.connect(server_address)

try:
    #Send data
    message = 'This is the message. It will be repeated.<EOF>'
    print >>sys.stderr, 'sending %s' % message
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()