'''
Created on Feb 24, 2014

@author: Savani Bharat
'''
class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        if numargs < 1:raise TypeError('requires atleast one argument')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
            
        elif numargs == 2:
            (self.start,self.stop)=args
            self.step=1
        elif numargs == 3:
            (self.start,self.stop,self.step)=args
        else: raise TypeError("Expected atmost 3 args,got {}".format(numargs))
        
        
        
# makes an object, iterable object
    def __iter__(self):
        i=self.start
        while i<=self.stop:
            yield i
            i+=self.step
            
def main():
    o=inclusive_range(5,25,5)
    for i in o:
        print i,
'''
   for i in inclusive_range(5,25,5):
        print i,

'''
if __name__=="__main__":main()
'''
o=inclusive_range(25)
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

o=inclusive_range(5,25)
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

o=inclusive_range(5,25,5)
5 10 15 20 25



'''

