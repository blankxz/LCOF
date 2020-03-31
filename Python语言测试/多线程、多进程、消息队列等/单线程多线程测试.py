import threading
import time

def ticks():
    c = 1
    for i in range(100000000):
        c += i

def oneThread():
    ticks()
    ticks()

def doubleThread():
    a = threading.Thread(target=ticks)
    b = threading.Thread(target=ticks)
    a.run()
    b.run()

time_start=time.time()
oneThread()
time_end=time.time()
print('totally cost',time_end-time_start)
time_start=time.time()
doubleThread()
time_end=time.time()
print('totally cost',time_end-time_start)