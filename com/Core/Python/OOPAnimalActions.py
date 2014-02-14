'''
Created on Feb 13, 2014

@author: Savani Bharat
'''

class AnimalActions:
    def quack(self): return self.strings['quack']
    def feathers(self): return self.strings['feathers']
    def bark(self): return self.strings['bark']
    def fur(self): return self.strings['fur']
    
class Duck(AnimalActions):
    strings = dict(
                 quack="Quaaaaak",
                 feathers="The duck has gray and white feather",
                 bark="the duck cannot bark",
                 fur="The duck has no fur"
                 )
    
class Person(AnimalActions):
    strings = dict(
                 quack="The person imitates a duck",
                 feathers="The person takes a feather from the ground and shows it",
                 bark="The person says woof woof",
                 fur="The person puts on a fur coat" 
                 )
    
class Dog(AnimalActions):
    strings = dict(
                 quack="Dog cannot quack",
                 feathers="Dogs dont have feather",
                 bark="Arf!",
                 fur="Dog has white fur with black spots"
                 )
    
def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())
    
def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())
    
def main():
    donald = Duck()
    john = Person()
    fido = Dog()
    
    print("In the forest")
    for o in (donald, john, fido):
        in_the_forest(o)


    print("In the dog house")
    for o in (donald, john, fido):
        in_the_doghouse(o)
    
if __name__ == '__main__':main()    
'''
In the forest
Quaaaaak
The duck has gray and white feather
The person imitates a duck
The person takes a feather from the ground and shows it
Dog cannot quack
Dogs dont have feather
In the dog house
the duck cannot bark
The duck has no fur
The person says woof woof
The person puts on a fur coat
Arf!
Dog has white fur with black spots
'''