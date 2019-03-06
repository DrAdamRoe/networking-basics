### adapted from https://github.com/realpython/materials/tree/master/python-sockets-tutorial
## and from https://stackoverflow.com/questions/21153262/sending-html-through-python-socket-server
## best source on HTTP standards is of course MDN: https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
port_number = 65432  # Port to listen on (non-privileged ports are > 1023)

def form_http_response():

    ## http start line
    start_line = "HTTP/1.0 200 OK\n"

    # The extendable list of HTTP headers
    headers = "Content-Type: text/html\n"

    # break between head and body - the neck, if you will.
    end_of_metadata="\n"

    # message payload, or body
    http_body = """
<html>
<body>
<h1>Hello World</h1>
<p>this is my server, hey.</p>
</body>
</html>
"""
    # set body length in header
    headers += "Content-Length: %i\n" % len(http_body.encode())

    # the "head": start-line + headers
    http_head = start_line + headers

    http_response = http_head + end_of_metadata + http_body

    return http_response


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

            # send encoded http response
            connection.send((form_http_response()).encode())

            # close connection
            connection.close()

            # kill server
            break
