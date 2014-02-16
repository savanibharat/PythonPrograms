'''
Created on Feb 15, 2014

@author: Savani Bharat
'''

import json
import pymongo
import urllib2

connection = pymongo.Connection("monogdb://localhost",safe=True)
db=connection.reddit
stories=db.stories

reddit_page=urllib2.urlopen("http://www.reddit.com/r/technology/.json")

parsed=json.loads(reddit_page.read())

for item in parsed['data']['children']:
    stories.insert(item['data'])