#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nikeah
#
# Created:     17/06/2014
# Copyright:   (c) Nikeah 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import cPickle as Pickle
import socket
import sys

def main():
    host = sys.argv[1]
    port = int(sys.argv[2])
    
    udpListener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpListener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udpListener.bind((host, port))
    
    data, addr = udpListener.recvfrom(1024)
    theTask = Pickle.loads(data)
    ans = theTask.Calculate()
    print ans

    udpListener.close()
    
    senderSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    senderSocket.sendto(str(ans), (addr[0], 8086))
    senderSocket.close()

if __name__ == '__main__':
    main()
