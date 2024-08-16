# a) type

string = "toto"
number = 10

string.encode('utf-8')
float(number)

string = string[::-1]
number = str(number)[::-1]
print(string,number)

# b) List

list = [1, 3, 2, 7, 4, 10, 46]
listA = list
listB = listA[2:5]
print(listB)

listC = listA + listB
listD = zip(listA , listB)

listA.append(5)
listC.append(None)
print(listC)

lst = [1,2,3]
n = 3

def conctener(lst,n = 2):
    concat = []
    for list in range(0,n):
        concat += lst
                
    print(concat)
    
conctener(lst)
        
while listC:
    list = listC.pop(0)
    print(list)
    
def evenNumbers(array):
    nbrEven = 0
    for number in array:
        isEven = number%2
        if isEven == 0:
            nbrEven +=1
            
    return nbrEven

print(evenNumbers(listA))


#C = [element for element in A if element %2 == 0]
C= []

for element in listA:
    if element %2 ==0:
        C.append(element)
        
def firstLetter(str):
    return str[0]

print(firstLetter('hello'))

#c) Dictionaries
"""

key	value
brand	Ford
model	Mustang
year	1964
"""

dictionary = {
    'brand':'Ford',
    'model':'Mustang',
    'year' : 1964
}

print(dictionary['year'])

for key in dictionary.keys():
    print(key)

for value in dictionary.values():
    print(value)
    
for index, (key,value) in enumerate(dictionary.items()):
    print("#{} - {} : {} ".format(index,key,value))

# d) Functions

def fibonacci(num):
    lastnumber = 0
    sum = 0
    result =''
    for number in range(0,num+1):
        oldsum = sum
        sum = sum +  lastnumber   
        
        if lastnumber == 0 :             
            lastnumber = 1
        else:
            lastnumber = oldsum
               
        result += "{} ,  ".format(sum)

    return result
        
print(fibonacci(10))