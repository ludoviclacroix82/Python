# Parent class
from dog_walking import Walk

class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True  # Instance attribute
        self.objet = Walk(name)  

    # Instance method
    def description(self):
        return "{} is {}.".format(self.name, self.age)

    # Instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
    
    # Method to change is_hungry to False
    def eat(self):
        self.is_hungry = False
        
    # Correction de l'indentation de la méthode walk
    def walk(self):
        return self.objet.walk()

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# New class to hold instances of dogs
class Pets:
    def __init__(self, dogs):
        self.dogs = dogs
        
    def count(self):
        return len(self.dogs)
    
    def speciesPets(self):
        return self.dogs[0].species  

# Create instances of dogs
my_dogs = [
    Bulldog("Tom", 6),
    RussellTerrier("Fletcher", 7),
    Dog("Larry", 9)
]

# Instantiate the Pets class with the list of dog instances
my_pets = Pets(my_dogs)

print("I have {} dogs.".format(my_pets.count()))

# Feed each dog
for dog in my_pets.dogs:
    dog.eat()

# Output the required information
for dog in my_pets.dogs:
    print(dog.description())
    print(dog.walk())

print("And they're all {}, of course".format(my_pets.speciesPets()))

# Check if all dogs are hungry or not
if all(dog.is_hungry for dog in my_pets.dogs):
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry.")
