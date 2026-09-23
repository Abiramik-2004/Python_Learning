'''
Multi-Theading:
    Maximize the performance of the CPU optimization

'''
class Hai:
    def hai(self):
        for i in range(100):
            print("Hai")
class Hello:
    def hello(self):
        for i in range(100):
            print("Hello")

obj1=Hai()
obj2=Hello()
obj1.hai()
obj2.hello()

#====================
from threading import Thread
import time
class MyThread(Thread):
    def run(self):
        print("Hai")
        time.sleep(3)

t=MyThread()
t.start()

#======================================

from threading import *
class HelloThread(Thread):
    def run(self):
        for i in range(5):
            print("Hiiii.......")

t=HelloThread()
t.start()
t.join()# it will releases the another thread
print("Thread completion....")

