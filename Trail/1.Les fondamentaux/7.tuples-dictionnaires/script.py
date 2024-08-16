dictionary = {    
    "sun":"Soleil",
    "moon":"Lune",
    "earth":"Terre",
    "hello":"salut",
    "bye":"Au revoir"
}


dictionary['good'] = 'Bien'
print(dictionary)


sentence = "I am the master of the world"
words = sentence.split(" ")

print(words)

universalNumber =  "The_universal_number_is_42" 
universal = universalNumber.replace("_"," ")

print(universal)


heroes = {"Superman" : "Clark kent", "Batman" : "Bruce Wayne", "Spiderman" : "Tony Parker"}

for heroe in heroes.values():
    print(heroe)
    
for heroe in heroes.keys():
    print(heroe)
    
heroes['Peter Parker'] = heroes.pop("Spiderman")

print(heroes)


items = {
    'Laser sword' : 229.0,
    'Mitendo DX' : 127.30,
    'Linux cushion' : 74.50,
    'Goldorak briefs' : 29.90,
    'Nextpresso station' : 184.60
}

totalPrice = 0

for price in items.values():
    totalPrice += price
    
print(totalPrice)

del items['Linux cushion']
print(items)

