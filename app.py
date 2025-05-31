from scanner.scanner import client_connection

print("=========================================")
ip_address  = input("Enter the target IP address: ").strip()

while ip_address == "":

        print("=========================================")
        print("The IP address cannot be an empty value!")
        print("=========================================")
        ip_address  = input("Enter the target IP address: ").strip()

print("=========================================")
starting_port  = input("Enter the starting port: ").strip()

while starting_port == "":
        
    print("=========================================")
    print("The starting port cannot be an empty value!")
    print("=========================================")
    starting_port  = input("Enter the starting port: ").strip()

print("=========================================")
ending_port = input("Enter the ending port: ").strip()
print("=========================================")

while ending_port == "":
        
    print("=========================================")
    print("The ending port cannot be an empty value!")
    print("=========================================")
    ending_port  = input("Enter the ending port: ").strip()

if __name__ == '__main__':
    client_connection(ip_address,(starting_port,ending_port))