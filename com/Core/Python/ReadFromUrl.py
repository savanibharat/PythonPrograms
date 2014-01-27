'''
Created on Jan 26, 2014

@author: Savani Bharat
'''

'''import urllib
response = urllib.urlopen("127.0.0.1")
html=response.read
print(html)'''
import urllib2
request = urllib2.Request('http://google.com')
response = urllib2.urlopen(request)
html = response.read()
print html

'''
import urllib
response = urllib.open('http://python.org')
html = response.read()

If you are using urllib2:

import urllib2
response = urllib2.urlopen('http://python.org')
html = response.read()

and if you wanna use the Request object:

request = urllib2.Request('http://python.org')
response = urllib2.urlopen(request)
html = response.read()
'''
