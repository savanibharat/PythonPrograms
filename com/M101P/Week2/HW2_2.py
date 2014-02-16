'''
Created on Feb 16, 2014

@author: Savani Bharat
'''
import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)
db = connection.students
grades = db.grades
#.sort('score', pymongo.ASCENDING)
def delteR():
    try:
        i = 0
        while i < 200:
            cursor = grades.find({'student_id':i})
            cursor = cursor.limit(5)
            # cursor=cursor.sort('score',pymongo.ASCENDING).skip(4).limit(1)
            cursor = cursor.sort([('score', pymongo.ASCENDING)]).limit(1)
            for doc in cursor:
                print doc
                cursor.remove(cursor.sort([('score', pymongo.ASCENDING)]).limit(1))
                break
            i = i + 1

    except:
        print("exception",sys.exc_info()[0])
        
delteR()