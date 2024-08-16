students =  ["Merouane", "Baptiste", "Caroline", "Joe", "Sophie", "Nathan", "Raphaël", "Axel", "Mathieu", "Adrien"]
studentsOrder = sorted(students)

# for student in studentsOrder:
#     print(student)

# for student in studentsOrder:
#     if student[:1] == 'M':
#         print(student)

# for number in range(0,15):
#     print(number)

# for number in range(0,10):
#     if number == 5:
#         break
    
#     print(number)

# for number in range(0,10):
#     if number == 5:
#         continue
    
#     print(number)

listOfnum = [17, 38, 10, 25, 72]
listOfnum.sort()
listOfnum.append(12)
print(listOfnum)
listOfnum.reverse()
print(listOfnum)
print(listOfnum.index(17))
listOfnum.remove(38)
print(listOfnum)
print(listOfnum[2:4])
print(listOfnum[0:+3])
print(listOfnum[-3])
print(listOfnum[-1:])

# number = int(input('Number :  '))

# for num in range(number+1)[::-1]:
#     print(num)
    
# number = 10

# prompt = int(input('number : '))

# while prompt != number :
#     if prompt > number :
#         print("It's less")
#     else:
#         print("It's more")

#     prompt = int(input('number : '))
    
print("Well done, you won")
       
allStudents =  [["David", "Justine", "Valentin","Axel", "Redouane"], ["Julie", "Stéphane", "Mostapha", "Claudiu", "Son"]]

for students in allStudents:
    for student in students:        
        print(" {} is a alumni. ".format(student))
        
languages = [["PHP", "Java", "C#"], ["HTML", "CSS", "Javascript"]]

for i in range(len(languages)):
    for language in languages[i]:
        if i == 0:
            print(" {} is a backend language".format(language))
        else:
            print(" {} is a frontend language".format(language))