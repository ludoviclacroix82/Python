def hello(name = 'Anonymous'):
    return "Hello {}".format(name)
    
hello()
hello('ludovic')

def sumOfStudents(students):
    studentsNumber = 0    
    
    for studentGrp in students:
        studentsNumber += len(studentGrp)


    return studentsNumber   

print(sumOfStudents([["Jean", "Alice", "Edwige", "Peter", "James"],
               ["Redouane", "Justine", "Adrien", "Nicolas", "Pierre"]]))



def is_divisible(n,x,y):

    divisibleX = n % x
    divisibleY = n % y
    
    if divisibleX == 0 and divisibleY == 0 :
        return True
    else:
        return False
    

print(is_divisible(3,1,3))
print(is_divisible(12,2,6))
print(is_divisible(100,5,3))
print(is_divisible(12,7,5))

def abbrevName(name):
    
    splitName = name.split(" ")     
    return "{}.{}".format(splitName[0][0],splitName[1][0])
    
    
print(abbrevName('Sam Harris'))

numbers = [1,-4,7,12]

def positive_sum(numbers):
    sum = 0
    
    for number in numbers:
        if int(number) >=0:
            sum += number
    
    return sum
    
print(positive_sum(numbers))

sunMix = ['5', '0', 9, 3, 2, 1, '9', 6, 7]

def sum_mix(sunMix):
    sum = 0
    
    for number in sunMix:
        if int(number) >=0:
            sum += int(number)
    return sum

print(sum_mix(sunMix))

num = input('please enter a number between 1 and 7 : ')
days = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

# while int(num) > 7 or int(num) < 1:
#     num = input('please enter a number between 1 and 7 : ')

def whatday(num):
    num = int(num)
    
    if num > 6 or num < 1:
        return "Wrong, please enter a number between 1 and 7"
    else:
        return days[num-1]    

print(whatday(num))

num = 2

def summation(num):
    sum = 0
    
    for number in range(1,num+1):
        sum += number
        
    return sum

print(summation(num))


n = 5

def count_sheep(n):
    murmur = ''
    
    for sheep in range(1,n+1):
        murmur += "{} sheep...".format(sheep)
        
    return murmur
        
print(count_sheep(n))

def final_grade(exam, projects):
    exam = int(exam)
    projects = int(projects)
    
    match (exam, projects):
        
        case _ if exam >90 or projects > 10:
            return 100
        case _ if exam >75 or projects >= 5:
            return 90
        case _ if exam >50 or projects >= 2:
            return 75        
        case _:
            return 0
        
print(final_grade(90, 10))

import unittest
 
class TestNotebook(unittest.TestCase):
    
    def test_hello(self):
        self.assertEqual(hello(),'Hello Anonymous')
        self.assertEqual(hello("Jean"),'Hello Jean')
    
    def test_sumOfStudents(self):
        self.assertEqual(sumOfStudents([["Jean", "Alice", "Edwige", "Peter", "James"],["Redouane", "Justine", "Adrien", "Nicolas", "Pierre"]]), 10)
        
 
    def test_is_divisible (self):
        self.assertEqual(is_divisible(3,3,4),False)
        self.assertEqual(is_divisible(12,3,4),True)
        self.assertEqual(is_divisible(8,3,4),False)
        self.assertEqual(is_divisible(48,3,4),True)

    
    def test_abbrevName(self):
        self.assertEqual(abbrevName("Sam Harris"), "S.H");
        self.assertEqual(abbrevName("Patrick Feenan"), "P.F");
        self.assertEqual(abbrevName("Evan Cole"), "E.C");
        self.assertEqual(abbrevName("P Favuzzi"), "P.F");
        self.assertEqual(abbrevName("David Mendieta"), "D.M");

    
    def test_positive_sum(self):
        self.assertEqual(positive_sum([1,2,3,4,5]),15)
        self.assertEqual(positive_sum([1,-2,3,4,5]),13)
        self.assertEqual(positive_sum([-1,2,3,4,-5]),9)
        self.assertEqual(positive_sum([]),0)
        self.assertEqual(positive_sum([-1,-2,-3,-4,-5]),0)
    
    def test_sum_mixed_array(self):
        self.assertEqual(sum_mix([9, 3, '7', '3']), 22)
        self.assertEqual(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]), 42)
        self.assertEqual(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']), 41)
        self.assertEqual(sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']), 45)
        self.assertEqual(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)
    
    def test_return_day(self):
        self.assertEqual(whatday(1), 'Sunday')
        self.assertEqual(whatday(2), 'Monday')
        self.assertEqual(whatday(3), 'Tuesday')
        self.assertEqual(whatday(8), 'Wrong, please enter a number between 1 and 7')
        self.assertEqual(whatday(20), 'Wrong, please enter a number between 1 and 7')
    
    def test_final_grade(self):
        self.assertEqual(final_grade(100, 12), 100)
        self.assertEqual(final_grade(85, 5), 90)
    
    def test_count_sheep(self):
        self.assertEqual(count_sheep(1), "1 sheep...");
        self.assertEqual(count_sheep(2), "1 sheep...2 sheep...")
        self.assertEqual(count_sheep(3), "1 sheep...2 sheep...3 sheep...")
        
    def test_summation(self):
        self.assertEqual(summation(1), 1)
        self.assertEqual(summation(8), 36)

unittest.main(argv=[''], verbosity=2, exit=False)