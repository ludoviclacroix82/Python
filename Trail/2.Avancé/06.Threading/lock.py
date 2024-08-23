from threading import Thread, RLock

lock = RLock()

class SyncThread(Thread):
    namefile = 'synch_thread.txt' 
    isLastThread = False
    
    def __init__(self, text , lastThread = False):
        Thread.__init__(self)
        self.text = text
        self.lastThread = lastThread
    
    def run(self):
        with lock:
            with open(self.namefile, 'a') as file:
                file.write(self.text)
            # print(self.lastThread)
            if self.lastThread:
                print(self.readFile()) 
                
    def readFile(self = None):           
            f = open(SyncThread.namefile)
            content = f.read()
            f.close()
            return content
                
thread_1 = SyncThread("Thread 1 /")
thread_2 = SyncThread("Thread 2 /")
thread_3 = SyncThread("Thread 3 /")
thread_4 = SyncThread("Thread 4 /",True)

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

# thread_1.join()
# thread_2.join()
# thread_3.join()
# thread_4.join()


# print(SyncThread.readFile())