'''
Created on Feb 13, 2014

@author: Savani Bharat
'''
def main():
    d={"a":1,"b":2,"c":3,"d":4,"e":5}
    for k in d:
        print(k,d[k])
    
    print 
    print
    d={"a":1,"b":2,"c":3,"d":4,"e":5}
    for k in sorted(d.keys()):
        print(k,d[k])
        
    print 
    print  
    d=dict(
           one=1,two=2,three=3,four=4
           )
    for k in sorted(d.keys()):
        print(k,d[k])
    
    
if __name__=="__main__":main()