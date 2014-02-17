'''
Created on Feb 16, 2014

@author: Savani Bharat
'''
def main():
    for i in inclusive_range(0, 25, 1):
        print i, 

def inclusive_range(start,stop,step):
    i=start
    while i<=stop:
        yield i
        i+=step

if __name__=="__main__":main()

'''
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

'''