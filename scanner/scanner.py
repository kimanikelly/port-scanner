import socket
from socket import AF_INET
from socket import SOCK_STREAM

def client_connection(ip_address=str,port=tuple[int]): 

    for port in range(port[0],port[1]):

        socket_instance = socket.socket(AF_INET,SOCK_STREAM)

        if socket_instance.connect_ex((ip_address,port)) == 0:
            print(port)
        
client_connection("127.0.0.1",(1,10000))

