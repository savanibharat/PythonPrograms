'''
Created on Feb 16, 2014

@author: Savani Bharat
'''
import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)
db = connection.school
people = db.people

print("insert in action")
richard = {"name":"Richard Kreuter", "company":"10gen",
        "interests":["horses", "skydiving", "fencing"]}

andrew={"_id":"erlichson","name":"Andrew Erlichson", "company":"10gen",
        "interests":["running","cycling","photography"]}

try:
    people.insert(richard)
    people.insert(andrew)
    
except:
    print("Exception occured",sys.exc_info()[0])
    
print(richard)
print(andrew)

'''
After running this program twice
> db.people.find().pretty()
{
        "_id" : ObjectId("530073669f8ededecdc8b9b8"),
        "interests" : [
                "horses",
                "skydiving",
                "fencing"
        ],
        "company" : "10gen",
        "name" : "Richard Kreuter"
}
{
        "_id" : "erlichson",
        "interests" : [
                "running",
                "cycling",
                "photography"
        ],
        "company" : "10gen",
        "name" : "Andrew Erlichson"
}
> db.people.find().pretty()
{
        "_id" : ObjectId("530073669f8ededecdc8b9b8"),
        "interests" : [
                "horses",
                "skydiving",
                "fencing"
        ],
        "company" : "10gen",
        "name" : "Richard Kreuter"
}
{
        "_id" : "erlichson",
        "interests" : [
                "running",
                "cycling",
                "photography"
        ],
        "company" : "10gen",
        "name" : "Andrew Erlichson"
}
{
        "_id" : ObjectId("530073aa9f8ede7f9d5a5080"),
        "interests" : [
                "horses",
                "skydiving",
                "fencing"
        ],
        "company" : "10gen",
        "name" : "Richard Kreuter"
}
'''
