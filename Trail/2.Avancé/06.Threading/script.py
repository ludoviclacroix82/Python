import time
from threading import Thread

class ThreadFunction(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
    
    def run(self):
        print("Thread {}: starting".format(self.name))
        time.sleep(2)
        print("Thread {}: finishing".format(self.name))

for i in range(5):
    thread = ThreadFunction(i)
    thread.start()