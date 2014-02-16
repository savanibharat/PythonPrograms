'''
Created on Feb 15, 2014

@author: Savani Bharat
'''
import pymongo
import sys

connection=pymongo.Connection("mongodb://localhost",safe=True)

db=connection.course
scores=db.scores

def LtGt():
    
    try:
        query={"type":"exam","score":{"$gte":35,"$lte":50}}
        selector={"_id":0}
        iter=scores.find(query,selector)
    except:
        print("Exception occured",sys.exc_info()[0])
    
    sanity=0
    for doc in iter:
        print doc
        sanity+=1
        if sanity>10:
            break
        
        
LtGt()
'''
{u'score': 40.0, u'type': u'exam', u'student': 1.0}
{u'score': 46.0, u'type': u'exam', u'student': 8.0}
{u'score': 41.0, u'type': u'exam', u'student': 17.0}
{u'score': 36.0, u'type': u'exam', u'student': 24.0}
{u'score': 42.0, u'type': u'exam', u'student': 29.0}
{u'score': 50.0, u'type': u'exam', u'student': 34.0}
{u'score': 39.0, u'type': u'exam', u'student': 36.0}
{u'score': 35.0, u'type': u'exam', u'student': 38.0}
{u'score': 35.0, u'type': u'exam', u'student': 43.0}
{u'score': 40.0, u'type': u'exam', u'student': 50.0}
{u'score': 39.0, u'type': u'exam', u'student': 60.0}
'''