'''
Created on Feb 13, 2014

@author: Savani Bharat
'''
class Fibonnaci():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def series(self):
        while(True):
            yield(self.b)
            self.a,self.b=self.b,self.a+self.b
    
f=Fibonnaci(0,1)
for r in f.series():
    if r>50:break
    print(r)

'''
1
1
2
3
5
8
13
21
34
'''       