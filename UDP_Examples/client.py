import socket

TCP_IP = socket.gethostname()
TCP_PORT = 13579

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((TCP_IP, TCP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print("received message: %s" % data)
