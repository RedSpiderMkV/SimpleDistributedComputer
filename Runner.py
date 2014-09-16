#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      RedSpiderMkV
#
# Created:     17/06/2014
# Copyright:   (c) RedSpiderMkV 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import cPickle as Pickle
import socket
import sys

class UdpCommunicator:
    host = ''
    port = 0
    
    replyAddress = ''
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        
        self.udpListener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udpListener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.udpListener.bind((host, port))
        
    def GetAndRunTask(self):
        data, addr = self.udpListener.recvfrom(1024)
        theTask = Pickle.loads(data)
        ans = theTask.Calculate()
        
        self.udpListener.close()
        self.replyAddress = addr[0]
        
        return ans
        
    def SendResponse(self, ans):
        senderSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        senderSocket.sendto(str(ans), (self.replyAddress, 8086))
        senderSocket.close()
        

def main():
    host = sys.argv[1]
    port = int(sys.argv[2])
    
    taskRunner = UdpCommunicator(host, port)
    taskResult = taskRunner.GetAndRunTask()
    
    print taskResult

    taskRunner.SendResponse(taskResult)

if __name__ == '__main__':
    main()
