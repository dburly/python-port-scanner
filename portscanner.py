#!/bin/python3

import sys
import socket
from datetime import datetime

#Define Our Target

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print('INVALID AMOUNT OF ARGUEMENTS')
	print('SYNTAX: python3 portscanner.py <ip>')

ports = []

#Add a pretty banner
print('-' * 50)
print('Scanning target: ' + target)
print('Time Started: ' + str(datetime.now()))
print('-' * 50)
try:
	for port in range(50, 85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) # If we cannot connect to the port within 1 sec we move on
		print('Checking port {}'.format(port))
		result = s.connect_ex((target, port)) # Returns an error indicator
		if result == 0: # An open port returns 0 and a closed port returns 1
			ports.append(port)
		s.close()

except KeyboardInterrupt:
	print('\nExiting Program')
	sys.exit()

except socket.gaierror:
	print('\nHOSTNAME COULD NOT BE RESOLVED')
	sys.exit()

except socket.error:
	print('\n COULD NOT CONNECT TO SERVER')
	sys.exit()

for p in ports:
        print('Port {} is open'.format(p))
