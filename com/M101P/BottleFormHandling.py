'''
Created on Feb 5, 2014

@author: Savani Bharat
'''
import bottle

@bottle.route('/')
def home_page():
    mythings=['apple','pear','peach','banana']
    #return bottle.template('hello_world',username='Bharat', things=mythings)
    return bottle.template('hello_worldfruit',{'username':"Aryan",'things':mythings})

@bottle.post('/favorite_fruit')
def favorite_fruit():
    fruit=bottle.request.forms.get("fruit")
    #if(fruit==None or fruit==""):
    #   fruit="No fruit selected"
        
    return bottle.template('fruit_selection.tpl',{'fruit':fruit})

bottle.debug(True)
bottle.run(host='localhost',port=8080)