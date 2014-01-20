'''
Created on Jan 19, 2014

@author: Savani Bharat
'''

a=[1,2,3,-4,'a','abcd']
print a
a.append("new element")
print a
b=a
print b
c=a[:]
print c

b[0]="element changed"
print b
print a
print c

"""
[1, 2, 3, -4, 'a', 'abcd']
[1, 2, 3, -4, 'a', 'abcd', 'new element']
[1, 2, 3, -4, 'a', 'abcd', 'new element']
[1, 2, 3, -4, 'a', 'abcd', 'new element']
['element changed', 2, 3, -4, 'a', 'abcd', 'new element']
['element changed', 2, 3, -4, 'a', 'abcd', 'new element']
[1, 2, 3, -4, 'a', 'abcd', 'new element']
"""