import socket
import sys
from socket import AF_INET
from socket import SOCK_STREAM

def client_connection(ip_address=str,port=tuple[int]): 

    try:
        
        for port in range(int(port[0]),int(port[1])):

            socket_instance = socket.socket(AF_INET,SOCK_STREAM)
           
            if socket_instance.connect_ex((ip_address,port)) == 0:
                socket.setdefaulttimeout(0.1)

                print({
                    "Port":port,
                    "Status":"Open",
                    "Service":socket.getservbyport(port)
                })
            socket_instance.close()
        
    except socket.gaierror:

        print("Invalid Hostname")
        sys.exit()

    except ValueError:

        if type(port[0]) == str:
            print("The starting port cannot be a string!")
            print("=========================================")

        if type(port[1]) == str:
            print("The ending port cannot be a string!")
            print("=========================================")

    except socket.error:

        print({
            "Port":port,
            "Status":"Open",
            "Service":"Unknown"
        })
            
        