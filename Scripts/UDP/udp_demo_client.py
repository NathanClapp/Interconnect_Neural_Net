#Based on: https://www.binarytides.com/programming-udp-sockets-in-python/

# Echo client program
import socket	#for sockets
import sys	#for exit

# create dgram udp socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print('Failed to create socket')
	sys.exit()

host = 'localhost';
port = 50007;

while(1):
	msg = str.encode(input('Enter message to send : '))
	
	if msg:

	#Set the whole string
		s.sendto(msg, (host, port))

	else:
		continue