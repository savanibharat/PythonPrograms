'''
Created on Feb 5, 2014

@author: Savani Bharat
'''
import bottle

@bottle.route('/')
def home_page():
    return "Hello World"

@bottle.route('/testpage')
def test_page():
    return "This is the test page"

bottle.debug(True)
bottle.run(host='localhost',port=8080)