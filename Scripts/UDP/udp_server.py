#Based on: https://www.binarytides.com/programming-udp-sockets-in-python/
#remake this whole thing in Go?

import udp_resource_lib
import socket, sys, subprocess

#make udp server object that can be created or killed
#randomly generated, non-overlapping server id's

def udp_server(host='', port=1234, byte_buffer=1024):
        socket_object = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket_object.bind((host, port))
        print("port " + str(port) + " bound to udp server")

        while 1:
            data, addr = socket_object.recvfrom(byte_buffer)
            data = data.decode('utf-8')
            print(data)
            print(type(data))
            #parse_tensor
            #start process for listening on mkfifo
            #send to files (1 function, make run files beforehand)
                #takes parsed tensor and location for run files
            
            #end 
