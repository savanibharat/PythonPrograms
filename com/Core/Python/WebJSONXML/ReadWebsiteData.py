'''
Created on Feb 26, 2014

@author: Savani Bharat
'''
import urllib2

def main():
    #open a connection to url using urllib2
    webUrl=urllib2.urlopen("http://jsonlint.com/")
    
    #get a result code and print it
    print "result code is "+str(webUrl.getcode())
  
    #read the data from the URL and print it
    data=webUrl.read()
    print data
    
if __name__ == '__main__':main()
'''
result code is 200
<!doctype html> 
<html lang="en" manifest="jsonlint.manifest"> 
    <head>


whole web page in html
'''