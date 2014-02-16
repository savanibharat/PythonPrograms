'''
Created on Feb 15, 2014

@author: Savani Bharat
'''

import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)

db = connection.course
users = db.users

def findDoc():
    
    query = {'name':'Aryan'}
    selector = {'_id':0}
    
    try:
        
        iter = users.find(query,selector)
        sanity = 0
        for doc in iter:
            print(doc)
            sanity += 1
            if(sanity > 10):
                break
    except:
        print("Exception occured", sys.exc_info()[0])
    
        

findDoc()  
'''
{u'name': u'Aryan', u'location': u'Gujarat'}

'''