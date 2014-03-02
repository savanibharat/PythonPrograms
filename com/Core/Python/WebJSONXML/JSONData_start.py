'''
Created on Feb 26, 2014

@author: Savani Bharat
'''
import urllib2
import json

def printResults(data):
    # use the json module to load the string data into dictionary
    theJSON = json.loads(data)
    # now we can access the contents of the json like any other python object
    if "title" in theJSON["metadata"]:
        print theJSON["metadata"]["title"]
   
    print 
    print
    
    # count the number of event, plus the magnitude and each event name
    count = theJSON["metadata"]["count"];
    print str(count) + " events recorded"
    
    print 
    print
    
    # for each event, print the place where it occured
    for i in theJSON["features"]:
        print i["properties"]["place"]
    
    print 
    print
    
    # prints the events that only have a magnitude greater than 4
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print "%2.1f" % i["properties"]["mag"], i["properties"]["place"]
    
    print 
    print
    
    # print only the events where atleast 1 person reported feeling something
    print "Events that were felt"
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if(feltReports != None) & (feltReports > 0):
            print "%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) + " times"
            
    
def main():
    
    # this feed lists all easrthquake for the last day larger than mag 2.5
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    
    # open the URL and read the data
    webUrl = urllib2.urlopen(urlData)
    print webUrl.getcode()
    
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        # print our customized results
        printResults(data)
    
    else:
        print "Received and error from server, cannot retrive results" + str(webUrl.getcode())
    

if __name__ == '__main__':main()
'''
200
USGS Magnitude 2.5+ Earthquakes, Past Day


19 events recorded


67km SE of Punta Cana, Dominican Republic
32km ENE of , Azerbaijan
97km NNW of Road Town, British Virgin Islands
53km SW of Redoubt Volcano, Alaska
Drake Passage
52km NNW of Charlotte Amalie, U.S. Virgin Islands
53km NE of Road Town, British Virgin Islands
75km N of Kodiak, Alaska
85km NNW of Road Town, British Virgin Islands
25km S of McCord, Oklahoma
43km SSE of Butte, Alaska
138km NNW of Amukta Island, Alaska
43km ESE of Boca de Yuma, Dominican Republic
85km NNW of Talkeetna, Alaska
22km NNE of Enid, Oklahoma
20km S of Medford, Oklahoma
41km SSW of Jarm, Afghanistan
69km NW of Murakami, Japan
Easter Island region


4.1 32km ENE of , Azerbaijan
5.3 Drake Passage
6.1 138km NNW of Amukta Island, Alaska
4.2 41km SSW of Jarm, Afghanistan
4.4 69km NW of Murakami, Japan
4.8 Easter Island region


Events that were felt
3.3 25km S of McCord, Oklahoma  reported 4 times
6.1 138km NNW of Amukta Island, Alaska  reported 1 times
3.4 20km S of Medford, Oklahoma  reported 3 times
'''