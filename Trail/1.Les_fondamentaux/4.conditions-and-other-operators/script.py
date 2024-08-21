age = 42
adds = age + 10
divAge = age // 7

textDiv = "{} divided by 7 is equal {}".format(age , divAge)
restDiv = age - divAge
expDiv = restDiv ** 3

# intInput = input('int : ')
# typeIntInput = type(intInput)
# print(intInput , typeIntInput)

bottleMilk = 0.45
bottleCider = 3.85
bagFlour = 0.9
packetButter = 0.77
jarNutella = 1.87

orderPrice = (bottleMilk*2) + (bottleCider*3) + bagFlour + packetButter + jarNutella
print("{0:.2f}".format(orderPrice))

# allowanceMoney = input('Money')
allowanceMoney = 20
reste = float(allowanceMoney) - round(orderPrice,2)
message = ''

if reste > 0:
    message = "You have spent {0:.2f} you have left {1:.2f}".format(orderPrice,reste)
elif reste == 0 :
    message = "You are broke!"
else :
    message= "Sorry you're missing amountMissing euros"
    
print(message)

# val1 = int(input('Val1 : '))
# val2 = int(input('Val2 : '))     

# if val1 > val2:
#     print(val2)       
# else:
#     print(val1)
             
# str1 = input('str 1 :')
# str2 = input('str 2 :')

# lenStr1 = len(str1)
# lenStr2 = len(str2)

# if lenStr1 > lenStr2 :
#     print(str1)
# else:
#     print(str2)
    
# devis = input('devis € or $  ')

# while devis != '€' and devis != '$':
#     devis = input('devis € or $  ')

# amount = float(input('Amount: '))

# if devis == '$':
#     convert = amount * 0.9
#     print("{:.2f} € ".format(convert))
# else:
#     convert = amount * 1.1
#     print("{:.2f} $".format(convert))

studentsTuring = ["Redouane", "Justine", "Ruben", "Edouard"]
name = "Ruben"

if name in studentsTuring :
    print("You are at the turing's")
else:
    print("You are not part of the turing's")
    
radius = 10
pi = 3.14
volume = ((4*pi)/3) * radius**3

print(volume)