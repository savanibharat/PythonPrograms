'''
Created on Feb 4, 2014

@author: Savani Bharat
'''
import bottle 
import pymongo

# this is the handler for the default path of the web server

@bottle.route('/')
def index():
    
    # connect to mongoDB
    connection = pymongo.MongoClient('localhost', 27017)
    
   
    # database name is course
    db = connection.course

    # handle users collection

    users = db.users;

    item = users.find_one()

    
    return '<b>Hello %s!</b>' % item['name']

bottle.run(host='localhost', port=8082)
