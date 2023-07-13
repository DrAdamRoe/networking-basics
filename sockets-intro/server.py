### adapted from https://github.com/realpython/materials/tree/master/python-sockets-tutorial
## documentation at https://docs.python.org/3/library/socket.html
## more good info at https://docs.python.org/3/howto/sockets.html

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
port_number = 3000  # Port to listen on (non-privileged ports are > 1023)

# AF_INET: use an IPv4 address
# SOCK_STREAM: use a stream socket, e.g. TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as aSocket:
    aSocket.bind((HOST, port_number))
    aSocket.listen()
    print("server started at address %s on port %i" % (HOST, port_number))
    connection, address = aSocket.accept() ## accept incoming connection
    with connection:
        print("Client connected from: ", address)
        while True:
            data = connection.recv(1024) ## receive byte data from the socket
            if not data:
                break
            print("message from client: ", data.decode())
            msg_response = "server got your message: " + data.decode()
            connection.send(msg_response.encode())
