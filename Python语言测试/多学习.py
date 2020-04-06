import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm "+self.name+' @ '+str(i)
            print(msg)
def tessst():
    for i in range(5):
        t = MyThread()
        t.start()

tessst()