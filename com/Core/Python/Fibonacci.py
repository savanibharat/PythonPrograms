'''
Created on Jan 19, 2014

@author: Savani Bharat
'''




def fibonacci(limit):
    a = 0
    b = 1
    print a
    print b
    while limit - 2 != 0:  # limit -2 because we actually printed out first two number
        sum = a + b
        print sum
        a = b
        b = sum
        limit = limit - 1
    
limit = input("enter the limit")
fibonacci(limit)


"""
0
1
2
3
5
8
13
21
34
55
89

"""