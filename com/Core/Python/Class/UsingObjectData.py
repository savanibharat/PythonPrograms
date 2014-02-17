'''
Created on Feb 16, 2014

@author: Savani Bharat
'''
class Duck:
    def __init__(self,**kwargs):
        self.variable=kwargs
    
    def quack(self):
        print("quack quack")
        
    def walk(self):
        print("duck likes a walk")
    
    def set_variable(self,k,v):
        self.variable[k]=v
        
    def get_variable(self,k):
        return self.variable.get(k,None)
    
def main():
    donald=Duck(feet=10)
    print(donald.get_variable('feet'))
    donald.set_variable('color', 'white')
    print(donald.get_variable('color'))


if __name__=="__main__":main()

'''
Any number of arguments and any type of arguments can be accepted by tihs program
10
white

'''
    