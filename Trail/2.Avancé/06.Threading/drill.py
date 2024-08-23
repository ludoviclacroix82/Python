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
        with lock:
            with open(self.sonnet, 'r') as file:
                content = file.read()
                return content
    

path=os.path.abspath('data')
folder_path = path
arrayFile = []
num = []
pattern = r'\d+'


for path, dirs, files in os.walk(folder_path):
    for filename in files:
        match = re.search(pattern, filename)
        num.append(int(match.group()))
        arrayFile.append(filename)
        
print(num)

for i in range(0,len(arrayFile)):
    for j in range(1,len(arrayFile)):
        num1 = match = re.search(pattern, arrayFile[i])
        num2 = match = re.search(pattern, arrayFile[j])
        # print(int(num1.group()) ,int(num2.group()) )
        print(i,j)
        if int(num1.group()) > int(num2.group()) :
          arrayFile[i] , arrayFile[j] = arrayFile[j] , arrayFile[i]

num.sort()

print(arrayFile)

# for i in range(0,len(num)):
#     file = "data/data_part_{}.txt".format(num[i])
#     thread = Sonnets(file)
#     thread.start()