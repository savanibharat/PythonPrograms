'''
Created on Feb 15, 2014

@author: Savani Bharat
'''
import pymongo
import sys

#establish connection to database
connection=pymongo.Connection("mongodb://localhost",safe=True)

#get a handle to database
db=connection.course
users=db.users

def find():
    print("executing find()")
    
    try:
        cursor=users.find()
        
    except:
        print("Exception occured",sys.exc_info()[0])
    
    sanity=0
    for doc in cursor:
        print doc
        sanity+=1
        if(sanity>10):
            break
        
        
def find_one():
    
    print("executing find_one()")
    query={"name":"Aryan"}
    
    try:
        doc=users.find_one(query)
        
    except:
        print("Exception occured",sys.exc_info()[0])
        
    print(doc)
    
find_one()


'''
find()
executing find()
{u'_id': ObjectId('52ddda816177f5dc6e3bc26d'), u'name': u'Aryan', u'location': u'Gujarat'}
{u'favorite_color': u'white', u'_id': ObjectId('52ddda5f6177f5dc6e3bc26c'), u'name': u'Bharat'}
{u'_id': ObjectId('52defaf707310b75f298ee1e'), u'name': u'richard', u'email': {u'personal': u'kreuter@example.com', u'work': u'richard@10gen.com'}}

executing find_one()
{u'_id': ObjectId('52ddda816177f5dc6e3bc26d'), u'name': u'Aryan', u'location': u'Gujarat'}




'''