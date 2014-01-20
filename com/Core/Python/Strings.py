'''
Created on Jan 19, 2014

@author: Savani Bharat
'''

a="this is a string"
print a
b="this string has single quote in it example java's work"
print b
c='this is string too'
print c
d='this string has double quotes "Name is Bond"'
print d

#remember you cannot enter single quote in string that you used in c or d
#remember you cannot enter double quotes in string that you used in a or b

a_with_b=a+b;
print a_with_b#this is a stringthis string has single quote in it example java's work


b_with_a=b+a
print b_with_a#this string has single quote in it example java's workthis is a string


print a.split(' ')#['this', 'is', 'a', 'string']
print a.split(" ")#['this', 'is', 'a', 'string']

print a.find("i")#2
print a.find('a')#8

f='3*4+5'
print f#3*4+5
print eval(f)#17
print eval(f+'1')#63 because 1 is attached to 5 so 3*4+51 =12+51=63

g="a+' '+b+' '+c+' '+d+' '+f"
print g#a+' '+b+' '+c+' '+d+' '+f
print eval(g)#this is a string this string has single quote in it example java's work this is string too this string has double quotes "Name is Bond" 3*4+5

a.replace('a', 'zz')
print a#output does not changes because we have not change the varialbe yet
a=a.replace('a', 'zz')#this is zz string
print a

print a.upper()#THIS IS ZZ STRING

print b.split('a')#['this string h', 's single quote in it ex', 'mple j', 'v', "'s work"]
print b.split(' ')#['this', 'string', 'has', 'single', 'quote', 'in', 'it', 'example', "java's", 'work']