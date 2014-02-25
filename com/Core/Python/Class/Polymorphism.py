'''
Created on Feb 24, 2014

@author: Savani Bharat
'''
class Duck:
    def quack(self):
        print("Duck:Quaaak")
    
    def walk(self):
        print("Duck:Walks like a duck")
        
    def bark(self):
        print("Duck: Duck cannot bark")
    
    def fur(self):
        print("Duck: Duck has feathers")
        
class Dog:
    def bark(self):
        print("Dog:Dog barks")
    
    def fur(self):
        print("Dog:THe dog has a brown and white fur")
        
    def quack(self):
        print("Dog:Dog barks")
    
    def walk(self):
        print("Dog:Dog walks like a dog")
        
def main():
    donald = Duck()
    fido = Dog()
    in_the_forest(fido)
    in_the_pond(donald)
    
    
def in_the_forest(dog):
    dog.bark()
    dog.fur()

def in_the_pond(duck):
    duck.quack()
    duck.walk()
    
    
if __name__ == "__main__":main()


'''
donald = Duck()
donald.quack()
donald.walk()
    
fido = Dog()
fido.bark()
fido.fur()
    
Duck:Quaaak
Duck:Walks like a duck
Dog:Dog barks
Dog:THe dog has a brown and white fur
----------------------------------------------
    donald = Duck()
    fido = Dog()
    
    for o in (donald,fido):
        o.quack()
        o.walk()
        o.bark()
        o.fur()

Duck:Quaaak
Duck:Walks like a duck
Duck: Duck cannot bark
Duck: Duck has feathers
Dog:Dog barks
Dog:Dog walks like a dog
Dog:Dog barks
Dog:THe dog has a brown and white fur
----------------------------------------------------
in_the_forest(fido)
    in_the_pond(donald)
    
    
def in_the_forest(dog):
    dog.bark()
    dog.fur()

def in_the_pond(duck):
    duck.quack()
    duck.walk()

Dog:Dog barks
Dog:THe dog has a brown and white fur
Duck:Quaaak
Duck:Walks like a duck

'''
