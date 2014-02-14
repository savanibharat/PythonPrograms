'''
Created on Feb 13, 2014

@author: Savani Bharat
'''
a, b = 1, 0
if(a < b):
    print('a ({}) is less than b ({})'.format(a, b))
else:
    print('b ({}) is less than a ({})'.format(b, a))
    
print("foo" if a < b else "bar")
