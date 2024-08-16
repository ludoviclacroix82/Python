alpha = 'Hello Wolrd!'
countAlpha = len(alpha)

countFloat = float(countAlpha)
reversedText = alpha[::-1]

pi = 3.14
roundPi = round(pi,10**2)

age = input('age :  ')
print(age,type(age))

text = 'Hello world !'
reversedText = list(text)
reversedText.reverse() 
print(reversedText)

num = [2, 8, 1, 4, 6, 3, 7] 
sortNum = sorted(num)
print(sortNum)
sumOfList = 0
for i in num:
    sumOfList += i

minValue = 0
maxValue = 0

minValue = min(num)
maxValue = max(num)

calc = "1 + 2"
result = eval(calc)
print(result) 

import unittest
 
class TestNotebook(unittest.TestCase):
 
    def test_countAlpha(self):
        self.assertEqual(countAlpha, 12)
    
    def test_countFloat(self):
        self.assertEqual(type(countFloat), type(float()))
        
    def test_pi(self):
        self.assertEqual(3.14, roundPi)
    
    def test_reversed(self):
        self.assertEqual(reversedText, ['!', ' ', 'd', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'H'])
    
    def test_age(self):
        self.assertEqual(type(age), type(str()))
        
    def test_sorted(self):
        self.assertEqual(sortNum, [1, 2, 3, 4, 6, 7, 8])
    
    def test_sum(self):
        self.assertEqual(sumOfList, 31)
    
    def test_min(self):
        self.assertEqual(minValue, 1)
    
    def test_max(self):
        self.assertEqual(maxValue, 8)
    
unittest.main(argv=[''], verbosity=2, exit=False)
