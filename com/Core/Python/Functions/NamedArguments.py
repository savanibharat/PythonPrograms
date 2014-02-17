'''
Created on Feb 16, 2014

@author: Savani Bharat
'''
def main():
    funct(1,2,3,43,44,45,one=1,two=2,three=3)
    

def funct(this, that, other,*args,**kwargs):
    print(this,that,other,args,kwargs)
    #args is tuple so they will be in sequence
    #kwargs is dictionary so they wont be in same order as we inserted
if __name__=="__main__":main()


'''
print(this,that,other,args,kwargs)
(1, 2, 3, (43, 44, 45), {'three': 3, 'two': 2, 'one': 1})


'''