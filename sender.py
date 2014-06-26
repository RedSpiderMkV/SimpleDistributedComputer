# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 11:22:51 2014

@author: User
"""

import socket
import cPickle as pickle
import SerialisableObject

host = 'localhost'
port = 8088
bufferSize = 4096
addr = (host, port)

udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

o = SerialisableObject.Task(21,5)

data = pickle.dumps(o)

udpSock.sendto(data, addr)

udpListener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpListener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udpListener.bind((host, 8086))

a, b = udpListener.recvfrom(1024)
print a, b

udpListener.close()
udpSock.close()