import socket

# We specify the IP of the server, not our own IP!
HOST = '192.168.56.1'
PORT = 99

# here we only have 1 socket for sending messages
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("Hello world!".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))