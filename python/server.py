# The server is going to be running all the time
import socket

HOST = '192.168.56.1'
# you could also specify the localhost here 
# HOST = '127.0.0.1'
# HOST = "localhost"

PORT = 99 # it's important to have the same port in the client and server

# dynamically getting the host:
# host = socket.gethostbyname(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

# specifies the number of unaccepted connections that the system will allow before refusing new connections
server.listen(5)

while True:
    # we accept all of the connections that we can have all the time

    # The return value is a pair (conn, address)
    # conn: new socket object usable to send and receive data on the 
    # connection (new socket for the connection)
    # address: of the incoming connection
    communication_socket, address = server.accept()

    # IMP: We don't use the server socket to talk to the client, we use the communication socket to talk to the client.
    # Thus for each new connection we get a new socket that allows us to communicate with this client because server socket here is just for accepting connections (NOT FOR THE COMMUNICATION IMP!)
    print("connected to", address)
    # we have to decode them because when we send them we send them in a byte stream
    # Byte-stream means that, as with pipes, there is no concept of message boundaries
    message = communication_socket.recv(1024).decode('utf-8')
    print("Message from client is:", message)
    communication_socket.send("Got your message, thank you!".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} ended successfully!")

# We did not cover multithreading here.
# So in this file it can only handle one connection at once