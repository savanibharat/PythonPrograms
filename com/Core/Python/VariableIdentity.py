'''
Created on Feb 13, 2014

@author: Savani Bharat
'''
x=42
print x,id(x)

y=2
print y,id(y)

z=42
print z,id(z)

print x==y
print x==z

print x is z 

z=dict(x=42)
print id(z)
print x==z