'''
Created on Feb 16, 2014

@author: Savani Bharat
'''
def main():
    funct(1,2,3,45,46,47,48)
    
def funct(this,that,other,*args):
    print(this,that,other)
    for n in args:
        print n,
    
if __name__=="__main__":main()

'''
args is tuple and tuple is immutable
print(this,that,other,args)
(1, 2, 3, (45, 46, 47, 48))


print(this,that,other)
    for n in args:
        print n,
(1, 2, 3)
45 46 47 48
'''