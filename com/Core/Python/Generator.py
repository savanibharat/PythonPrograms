'''
Created on Feb 13, 2014

@author: Savani Bharat
'''
def isPrime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True
    
def primes(n=1):
    while(True):
        if isPrime(n): yield n#a function that return object
        n+=1
        
for n in primes():
    if n>100:break
    print(n)
            
'''
Generators are iterators, but you can only iterate over them once. It's because they 
do not store all the values in memory, they generate the values on the fly:

mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)
    
Yield is a keyword that is used like return, except the function will return a 
generator.

Output:
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97

'''