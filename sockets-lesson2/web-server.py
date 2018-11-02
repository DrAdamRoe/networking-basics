### adapted from https://github.com/realpython/materials/tree/master/python-sockets-tutorial
## and from https://stackoverflow.com/questions/21153262/sending-html-through-python-socket-server

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
port_number = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, port_number))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data)
            #conn.sendall(data)
            conn.send('HTTP/1.0 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('\n') # header and body should be separated by additional newline
            conn.send("""
                <html>
                <body>
                <h1>Hello World</h1> this is my server!
                </body>
                </html>
                """) # Use triple-quote string.
            conn.close()
