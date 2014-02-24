'''
Created on Feb 22, 2014

@author: Savani Bharat
'''
import pymongo

connection=pymongo.Connection("mongodb://localhost",safe=True)
db=connection.school
students=db.students


cursor=students.find({},{'scores':1})

for entry in cursor:
    _id=entry['_id']
    scores=entry['scores']
    
    hwScores=[]
    
    for score in scores:
        if score['type']=='homework':
            hwScores.append(score['score'])
            
    hwScores.sort();
    
    scores.remove({'type':'homework','score':hwScores[0]})
    
    students.update({'_id':_id},{'$set':{'scores':scores}})
            