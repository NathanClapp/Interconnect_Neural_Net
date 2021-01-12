# Echo server program
import socket

host = ''                 # Symbolic name meaning all available interfaces
port = 50007              # Arbitrary non-privileged port

socket_object = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_object.bind((host, port))
print("port " + str(port) + " bound")

while 1:
    data, addr = socket_object.recvfrom(1024)
    print(data)
