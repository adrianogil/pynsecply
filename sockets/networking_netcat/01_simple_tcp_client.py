# http://bt3gl.github.io/black-hat-python-networking-the-socket-module.html
import socket

# HOST = 'www.google.com'
# PORT = 80
# DATA = 'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n'

HOST = '127.0.0.1'
PORT = 9090
DATA = 'GET / HTTP/1.1\r\n'

def tcp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.send(DATA)
    response = client.recv(4096)
    print response

if __name__ == '__main__':
    tcp_client()