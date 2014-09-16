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


import os
from threading import Thread

host = '192.168.0.11'
port = 8088
bufferSize = 4096
addr = (host, port)

runner = r'C:\Python27\python.exe Runner.py {0} {1}'

def executeRunner():
    os.system(str.format(runner, host, port))

def main():
    while True:
        t1 = Thread(target=executeRunner, args=())
        t1.start()
        t1.join()

if __name__ == '__main__':
    main()

#t1 = thread.start_new_thread(executeRunner, ())

#while True:
    #subprocess.Popen(["python", "runner.py"], stdout=subprocess.PIPE)
# a = raw_input('Enter 0 to exit')
# if a == '0':
# break;
