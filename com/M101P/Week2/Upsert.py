'''
Created on Feb 16, 2014

@author: Savani Bharat
'''
import pymongo
import sys

connection=pymongo.Connection("mongodb://localhost",safe=True)
db=connection.test
things=db.things

def using_upsert():
    print("updating with upsert")
    
    try:
        #things.drop()
        
        things.update({'thing':'apple'}, {'$set':{'color':'red'}}, upsert=True)
        things.update({'thing':'pear'}, {'color':'green'}, upsert=True)
        
        apple=things.find_one({'thing':'apple'})
        print "apple:",apple
        
        pear=things.find_one({'thing':'pear'})
        print "pear: ",pear
        
    except:
        print "Exception occured",sys.exc_info()[0]
        raise
    
using_upsert()

'''
updating with upsert
apple: {u'color': u'red', u'thing': u'apple', u'_id': ObjectId('5300812cc0b981293c4cebca')}
pear:  None

'''