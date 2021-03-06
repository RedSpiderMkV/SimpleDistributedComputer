#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      RedSpiderMkV
#
# Created:     16/06/2014
# Copyright:   (c) RedSpiderMkV 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import cPickle as Pickle
import socket
import Task

host = '192.168.0.2'
port = 8088
bufferSize = 4096
addr = (host, port)

udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

o = Task.SerialisableTestClass(2,5)

data = Pickle.dumps(o)

udpSock.sendto(data, addr)

udpListener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpListener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udpListener.bind(('192.168.0.11', 8086))

a, b = udpListener.recvfrom(1024)
print a, b

udpListener.close()
udpSock.close()