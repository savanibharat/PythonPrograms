'''
Created on Feb 14, 2014

@author: Savani Bharat
'''

def main():
    s="this is a string"
    for i,c in enumerate(s):
        #print('index-> {} has value-> {}'.format(i,c))
        if c=='s':print ('index-> {} has value-> {}'.format(i,c))
        
if __name__=="__main__":main()

'''
index-> 0 has value-> t
index-> 1 has value-> h
index-> 2 has value-> i
index-> 3 has value-> s
index-> 4 has value->  
index-> 5 has value-> i
index-> 6 has value-> s
index-> 7 has value->  
index-> 8 has value-> a
index-> 9 has value->  
index-> 10 has value-> s
index-> 11 has value-> t
index-> 12 has value-> r
index-> 13 has value-> i
index-> 14 has value-> n
index-> 15 has value-> g


index-> 3 has value-> s
index-> 6 has value-> s
index-> 10 has value-> s

'''