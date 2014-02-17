'''
Created on Feb 16, 2014

@author: Savani Bharat
'''
def main():
    print(returnvalue())
    
    for n in returnRange():
        print n,
    
    
def returnvalue():
    return 10

def returnRange():
    return range(25)

if __name__=="__main__":main()

'''
10
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24

'''