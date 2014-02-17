'''
Created on Feb 16, 2014

@author: Savani Bharat
'''
class Duck:
    def quack(self):
        print("quack quack")
    
    def walk(self):
        print("duck likes a walk")
        
def main():
    donald=Duck()
    print(donald)
    donald.quack()#donald.quack(donald) object donald gets in to the parameter by python itself we need not do it
    donald.walk()
    
if __name__=="__main__":main()
'''
<__main__.Duck instance at 0x000000000241E248>
quack quack
duck likes a walk

why to write self?
The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes. 
Python decided to do methods in a way that makes the instance to which the method belongs be passed automatically, 
but not received automatically: the first parameter of methods is the instance the method is called on. That makes 
methods entirely the same as functions, and leaves the actual name to use up to you (although self is the convention, 
and people will generally frown at you when you use something else.) self is not special to the code, it's just another object.


'''