'''
Created on Feb 13, 2014

@author: Savani Bharat
'''
class Egg:
    def __init__(self,kind="fried"):
        self.kind=kind #this will create object variable that will be carried around and encapsulated
        #in the object

    def whatKind(self):
        return self.kind

def main():
    fried=Egg() 
    print(fried.whatKind())
    scrambled=Egg('scrambled')
    print(scrambled.whatKind())
    
if __name__=="__main__": main()

'''
fried
scrambled

'''