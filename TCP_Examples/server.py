import socket
import time

TCP_IP = socket.gethostname()
TCP_PORT = 12345

LISTEN_QUEUE = 5
HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(LISTEN_QUEUE)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    msg = "Welcome to the server."
    msg = f'{len(msg):<{HEADER_SIZE}}' + msg

    clientsocket.send(bytes(msg, "utf-8"))

    while True:
            time.sleep(3)
            msg = f"The time is: {time.time()}"
            msg = f'{len(msg):<{HEADER_SIZE}}' + msg
            clientsocket.send(bytes(msg, "utf-8"))
