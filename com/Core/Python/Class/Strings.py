'''
Created on Mar 3, 2014

@author: Savani Bharat
'''
from string import count

string = "This is is a String String".lower().split(" ")

wordcount={}
for word in string:
    if word in wordcount:
            wordcount[word] += 1
    else:
            wordcount[word] = 1
        
for k,v in wordcount.items():
    print k, v

print wordcount
