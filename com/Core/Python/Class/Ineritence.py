'''
Created on Feb 16, 2014

@author: Savani Bharat
'''
class Animal:
    def walk(self):
        print('hey I''am walking here')
    def run(self):
        print('hey I''am running here')
    def fur(self):
        print('I have a fur')

class Duck(Animal):
    def walk(self):
        print('Duck likes to walk')
    
    def run(self):
        print('Duck is running')
        
class Dog(Animal):
    def run(self):
        pass

def main():
    donald=Duck()
    donald.walk()
    donald.run()
    
    print
    
    jagar=Dog()
    jagar.run()
    jagar.walk()

if __name__=="__main__":main()

'''
Duck likes to walk
Duck is running

hey Iam walking here
'''