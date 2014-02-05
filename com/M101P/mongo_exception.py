'''
Created on Feb 5, 2014

@author: Savani Bharat
'''
import sys
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.test
users = db.names

doc = {'firstname': 'King','lastname': 'queen'}
print doc
print "about to insert document"

try:
    users.insert(doc)
except:
    print "insert failed", sys.exc_info()[0]
    
#to insert again reassign doc
doc = {'firstname': 'King','lastname': 'queen'}
print doc
print"inserting again"

try:
    users.insert(doc)
except:
    print "second insert failed", sys.exc_info()[0]

    
print doc

'''
{'lastname': 'queen', 'firstname': 'King'}
about to insert document
{'lastname': 'queen', '_id': ObjectId('52f2a83c9f8ede4f88b2ee28'), 'firstname': 'King'}
inserting again
second insert failed <class 'pymongo.errors.DuplicateKeyError'>
{'lastname': 'queen', '_id': ObjectId('52f2a83c9f8ede4f88b2ee28'), 'firstname': 'King'}

---------------------------------------------------------------------------------------

After reassigning doc as per line #14

{'lastname': 'queen', 'firstname': 'King'}
about to insert document
{'lastname': 'queen', 'firstname': 'King'}
inserting again
{'lastname': 'queen', '_id': ObjectId('52f2a8b79f8ede7f84997c73'), 'firstname': 'King'}

Output in monog shell

> db.names.find().pretty()
{
        "_id" : ObjectId("52f2a8b79f8ede7f84997c72"),
        "lastname" : "queen",
        "firstname" : "King"
}
{
        "_id" : ObjectId("52f2a8b79f8ede7f84997c73"),
        "lastname" : "queen",
        "firstname" : "King"
}

'''
