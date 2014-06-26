# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 11:29:40 2014

@author: User
"""

import os
from threading import Thread

host = 'localhost'
port = 8088
bufferSize = 4096
addr = (host, port)

def executeRunner():
    os.system("runner.py")

while True:
    t1 = Thread(target=executeRunner, args=())
    t1.start()
    t1.join()
    
#t1 = thread.start_new_thread(executeRunner, ())

#while True:
    #subprocess.Popen(["python", "runner.py"], stdout=subprocess.PIPE)
#    a = raw_input('Enter 0 to exit')
#    if a == '0':
#        break;
