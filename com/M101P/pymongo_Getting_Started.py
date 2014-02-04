'''
Created on Feb 4, 2014

@author: Savani Bharat
'''
import pymongo

from pymongo import MongoClient

#connect to database
connection=MongoClient('localhost',27017)

#database name is course
db=connection.course

#handle users collection

users=db.users;

item=users.find_one()

print item['name']