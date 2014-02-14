'''
Created on Feb 13, 2014

@author: Savani Bharat
'''
def main():
    func(3)
    func()
    func(7)
def func(a=5):
    for i in range(a,10):
        print i,
    print
if __name__=="__main__":main()

'''
3 4 5 6 7 8 9
5 6 7 8 9
7 8 9
'''