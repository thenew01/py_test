#! /usr/bin/env python
#coding=utf-8
#coding=utf-8
#!/usr/bin/python

import threading
import time

exitFlag = 0

class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        print('Starting %s' % self.name)
        print_time(self.name, 1, self.counter)
        print('Exiting',   self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            thread.exit()
        time.sleep(delay)
        print('%s: %s' % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程

threads = []
for i in range(10):
    th = myThread(i, 'Thread-%s ' % i, 100)    
    th.start()
    threads.append(th)
    
for th in threads:
    th.join()


print("Exiting Main Thread")
