'''
Created on Feb 16, 2014

@author: Savani Bharat
'''
def main():
    for i in inclusive_range(25):
        print i,

def inclusive_range(*args):
    numargs = len(args)
    if numargs < 1: raise TypeError("Atleast 1 parameter required")
    
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    
    elif numargs == 2:
        (start, stop) = args
        step = 1
    
    elif numargs == 3:
        (start, stop, step) = args
    
    else:
        raise TypeError("Atmost 3 parameters are accepted. Too many Parameters")
        
    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == "__main__":main()
'''
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
'''
