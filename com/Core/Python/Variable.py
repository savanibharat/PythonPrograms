'''
Created on Feb 13, 2014

@author: Savani Bharat
'''
x = 12
print id(x)
print type(x)
print('----------------------')
x = 13
print id(x)
print type(x)
print('----------------------')
x = 12
print id(x)
print type(x)
print('----------------------')


y = "Abcd"
print id(y)
print type(y)
print('----------------------')
y="xyz"
print id(y)
print type(y)

'''
32760032
<type 'int'>
----------------------
32760008
<type 'int'>
----------------------
32760032
<type 'int'>
----------------------
37894344
<type 'str'>
----------------------
37895064
<type 'str'>
'''