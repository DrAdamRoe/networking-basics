## function to get local IP address of current machine 
## lifted from https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib 

import socket

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


print(get_ip())

