'''
Created on Feb 15, 2014

@author: Savani Bharat
'''
# 2     3    1
# Skip Limit Sort
import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)
db = connection.course
scores = db.scores

def find():
    print("find in action")
    
    query = {}
    try:
        # cursor = scores.find(query).sort('score', pymongo.ASCENDING).skip(4).limit(1)
        cursor = scores.find(query).skip(4)
        cursor = cursor.limit(5)
        # cursor=cursor.sort('score',pymongo.ASCENDING).skip(4).limit(1)
        cursor = cursor.sort([('score', pymongo.ASCENDING), ('type', pymongo.DESCENDING)])
        
    except:
        print("exception occured", sys.exc_info()[0])
        
    for doc in cursor:
        print doc
    

find()
'''
#cursor = scores.find(query).sort('score', pymongo.ASCENDING).skip(4).limit(1)
find in action
{u'_id': ObjectId('52de3dd16177f5dc6e3bc4dc'), u'type': u'essay', u'score': 0.0, u'student': 207.0}


cursor=scores.find(query).skip(4)
cursor=cursor.limit(1)
cursor=cursor.sort('score',pymongo.ASCENDING).skip(4).limit(1)
find in action
{u'_id': ObjectId('52de3dd16177f5dc6e3bc4dc'), u'type': u'essay', u'score': 0.0, u'student': 207.0}


cursor=cursor.sort([('score',pymongo.ASCENDING),('type',pymongo.DESCENDING)])
find in action
{u'_id': ObjectId('52de3dd16177f5dc6e3bc3b5'), u'type': u'exam', u'score': 0.0, u'student': 109.0}
{u'_id': ObjectId('52de3dd16177f5dc6e3bc442'), u'type': u'exam', u'score': 0.0, u'student': 156.0}
{u'_id': ObjectId('52de3dd16177f5dc6e3bc46c'), u'type': u'exam', u'score': 0.0, u'student': 170.0}
{u'_id': ObjectId('52de3dd16177f5dc6e3bc562'), u'type': u'exam', u'score': 0.0, u'student': 252.0}
{u'_id': ObjectId('52de3dd16177f5dc6e3bc80e'), u'type': u'exam', u'score': 0.0, u'student': 480.0}

'''
