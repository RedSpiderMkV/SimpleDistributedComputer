# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 09:55:00 2014

@author: User
"""

import cPickle as pickle
import socket

host = 'localhost'
port = 8088
bufferSize = 4096
addr = (host, port)


def main():
    
    udpListener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpListener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udpListener.bind((host, port))
    
    print 'waiting'

    data, addr = udpListener.recvfrom(bufferSize)
    
    d = pickle.loads(data)
    res = str(d.Calculate())
    print res

    udpListener.close()
    
    senderSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    senderSocket.sendto(res, (addr[0], 8086))
    senderSocket.close()
        
if __name__ == "__main__":
    main()