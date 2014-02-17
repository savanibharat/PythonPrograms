'''
Created on Feb 16, 2014

@author: Savani Bharat
'''
def main():
    
    try:
        
        fh=open("xlines.txt")
        
    except IOError as e:
        print("Exception occured:",e)
    
    else:
        for line in fh:
            print(line.strip())
    
if __name__=="__main__":main()