'''
Created on Feb 13, 2014

@author: Savani Bharat
'''
def isPrime(n):
    if n==1:
        print ("1 is special")
        return False
    for x in range(2,n):
        if n%x ==0:
            print("{} equals {}*{}".format(n,x,n//x))
            return False
    else:
        print(n, " is prime number")
        return True
    
for n in range(1,20):
    isPrime(n)
    
'''
1 is special
(2, ' is prime number')
(3, ' is prime number')
4 equals 2*2
(5, ' is prime number')
6 equals 2*3
(7, ' is prime number')
8 equals 2*4
9 equals 3*3
10 equals 2*5
(11, ' is prime number')
12 equals 2*6
(13, ' is prime number')
14 equals 2*7
15 equals 3*5
16 equals 2*8
(17, ' is prime number')
18 equals 2*9
(19, ' is prime number')

'''