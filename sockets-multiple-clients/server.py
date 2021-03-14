import socket
import threading

# Procedure ordered by numbers on top

# 1.
HEADER = 64  # This will represent 64 bytes
PORT = 5050
# socket.gethostbyname(socket.gethostname()) will get the IP address automatically for you
# [OPTIONAL] To connect to the internet, change SERVER's value to your public IP address
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


# 2.    - Open up socket to connect to other devices
#       - Bind socket to port and IP address
#       - AF_INET tells the socket that it must use an IPv4 address
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# 5.    [OPTIONAL] To send messages between clients, store the indiv messages globally & run new thread


# 4.    Handles indiv communication between client and server
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # convert from bytes to string using utf-8
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:  # blocking line
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()


# 3.    This function will allow our server to:
#           - listen to connections
#           - handle them
#           - pass them onto handle_client which will run in new thread
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # - Waits for new connection to server
        # - When new connection occurs:
        #       - it will store the IP and port as addr
        #       - it will store the socket object (as conn) which allows us send info back
        conn, addr = server.accept()  # blocking line
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()- 1}") 


print("[STARTING] server is starting...")
start()
