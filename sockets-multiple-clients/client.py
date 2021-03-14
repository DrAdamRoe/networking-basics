import socket

HEADER = 64  # 64 bytes
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = " " # Enter server's IP address
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("Hello First World!")
send("Hello Second World!")
send("Hello Third World!")
send("Hello Fourth World!")
send("Hello Fifth World!")
send(DISCONNECT_MESSAGE)

# run python client.py in about 3 seperate terminals, optionally on three seperate machines
