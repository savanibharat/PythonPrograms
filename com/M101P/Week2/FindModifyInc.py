'''
Created on Feb 16, 2014

@author: Savani Bharat
'''
import pymongo
import sys

def get_next_sequence_number(name):
    connection=pymongo.Connection("mongodb://localhost",safe=True)
    db=connection.test
    counters=db.counters
    
    counter=counters.find_and_modify(query={'type':name},
                                    update={'$inc':{'value':1}},
                                    upsert=True,new=True)
    
    counter_value=counter['value']
    return counter_value

print get_next_sequence_number('uid')
print get_next_sequence_number('uid')
print get_next_sequence_number('uid')
print get_next_sequence_number('uid')
print get_next_sequence_number('uid')

'''
Ran first time
1
2
3
4
5

Ran second time
6
7
8
9
10

Ran third time
11
12
13
14
15

'''