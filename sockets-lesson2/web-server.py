### adapted from https://github.com/realpython/materials/tree/master/python-sockets-tutorial
## and from https://stackoverflow.com/questions/21153262/sending-html-through-python-socket-server

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
port_number = 65433  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as aSocket:
    aSocket.bind((HOST, port_number))
    aSocket.listen()
    print("server started at address %s on port %i" % (HOST, port_number))
    connection, address = aSocket.accept()
    with connection:
        print("Client connected from: ", address)
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print("message from client: \n", data.decode())
            print(" -- end message from client -- \n")
            connection.send('HTTP/1.0 200 OK\n'.encode())
            connection.send('Content-Type: text/html\n'.encode())
            connection.send('\n'.encode()) # header and body should be separated by additional newline
            connection.send("""
                <html>
                <body>
                <h1>Hello World</h1> this is my server, damnit!
                </body>
                </html>
                """.encode())  # Use triple-quote string.
            connection.close()
