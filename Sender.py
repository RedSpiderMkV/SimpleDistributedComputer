#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nikeah
#
# Created:     16/06/2014
# Copyright:   (c) Nikeah 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import cPickle as Pickle
import socket
import Task

host = 'localhost'
port = 8088
bufferSize = 4096
addr = (host, port)

udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

o = Task.SerialisableTestClass(21,5)

data = Pickle.dumps(o)

udpSock.sendto(data, addr)

udpListener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpListener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udpListener.bind((host, 8086))

a, b = udpListener.recvfrom(1024)
print a, b

udpListener.close()
udpSock.close()