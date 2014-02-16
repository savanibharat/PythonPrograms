'''
Created on Feb 15, 2014

@author: Savani Bharat
'''
import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)
db = connection.course
scores = db.scores

def find():
    print("find in action")
    
    query={"type":{"$regex":"exam"}}
    projection={"_id":0}
    
    try:
        iter=scores.find(query,projection)
    
    except:
        print("Exception occured",sys.exc_info()[0])
    
    sanity=0
    for doc in iter:
        print(doc)
        sanity+=1
        if sanity>10:
            break

find()

'''
find in action
{u'score': 94.0, u'type': u'exam', u'student': 0.0}
{u'score': 40.0, u'type': u'exam', u'student': 1.0}
{u'score': 27.0, u'type': u'exam', u'student': 2.0}
{u'score': 100.0, u'type': u'exam', u'student': 3.0}
{u'score': 29.0, u'type': u'exam', u'student': 4.0}
{u'score': 56.0, u'type': u'exam', u'student': 5.0}
{u'score': 56.0, u'type': u'exam', u'student': 6.0}
{u'score': 84.0, u'type': u'exam', u'student': 7.0}
{u'score': 46.0, u'type': u'exam', u'student': 8.0}
{u'score': 61.0, u'type': u'exam', u'student': 9.0}
{u'score': 25.0, u'type': u'exam', u'student': 10.0}
'''