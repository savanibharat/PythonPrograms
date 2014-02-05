'''
Created on Feb 4, 2014

@author: Savani Bharat
'''
import sys

try:
    print 10/0
    
except:
    print "Exception ",sys.exc_info()[0]
    
print "this line will be printed"


'''
Exception  <type 'exceptions.ZeroDivisionError'>
this line will be printed
'''