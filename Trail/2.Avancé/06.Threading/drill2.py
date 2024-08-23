import os
import re
from threading import Thread, RLock

lock = RLock()

class Url(Thread):
    
    def __init__(self,url):
        Thread.__init__(self)
        self.url=url
        
    def run(self):
        with lock:
            print(self.url)
    


urls = [
  'http://www.python.org',
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
]

for i in range(0,len(urls)):
    url = Url(urls[i])
    url.start()