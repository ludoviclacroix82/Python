# Exercise 1

import os
import re
from threading import Thread, RLock

lock = RLock()

class Sonnets(Thread):
    
    namefile = 'data_all.txt'
    
    def __init__(self,sonnet):
        Thread.__init__(self)
        self.sonnet = sonnet
        
    def run(self):
        with lock:
            with open(self.namefile, 'a') as file:
                file.write("{} \n".format(self.read()))
                
    def read(self):
            with open(self.sonnet, 'r') as file:
                content = file.read()
                return content
    

path=os.path.abspath('data')
folder_path = path
arrayFile = []
pattern = r'\d+'


for path, dirs, files in os.walk(folder_path):
    for filename in files:
        match = re.search(pattern, filename)
        arrayFile.append(filename)

for i in range(0,len(arrayFile)):
    for j in range(0,len(arrayFile)-1):
        num1 = match = re.search(pattern, arrayFile[j])
        num2 = match = re.search(pattern, arrayFile[j+1])
        if int(num2.group()) < int(num1.group()) :
          arrayFile[j] , arrayFile[j+1] = arrayFile[j+1] , arrayFile[j]


for i in range(0,len(arrayFile)):
    file = "data/{}".format(arrayFile[i])
    thread = Sonnets(file)
    thread.start()