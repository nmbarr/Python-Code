import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 20777

s = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
s.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = s.recvfrom(2048)
    print(data)
