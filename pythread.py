#coding:utf-8 
'''
Created on 2015年3月3日

@author: MQ
'''
import threading
from time import sleep
import thread

NUM = 0

def countNum1():
    global NUM
    while 1:
        global mutex
        mutex.acquire()
        print "counter111:  %s \n"  %NUM
        NUM = NUM+1
        mutex.release()
        sleep(1)

def countNum2():
    global NUM
    while 1:
        global mutex
        mutex.acquire()
        print "counter222:  %s\n"  %NUM
        NUM = NUM+1
        mutex.release()
        sleep(2)

threads = []
t1 = threading.Thread(target=countNum1)
threads.append(t1)

t2 = threading.Thread(target=countNum2)
threads.append(t2)

if __name__ == '__main__':
    mutex = thread.allocate_lock()
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    
    
    