'''
Created on Feb 5, 2014

@author: Savani Bharat
'''

import bottle

@bottle.route('/')
def home_page():
    mythings=['apple','banana','peach','pear']
    return bottle.template('hello_world',username='Aryan',things=mythings)

bottle.debug(True)
bottle.run(host='localhost',port=8080)