'''
Created on Feb 16, 2014

@author: Savani Bharat
'''
class Duck:
    def __init__(self,value):
        self._v=value
    
    def quack(self):
        print("quack quack",self._v)
    
    def walk(self):
        print("duck likes a walk",self._v)
        
def main():
    donald=Duck(10)
    print(donald)
    donald.quack()
    donald.walk()
    print
    print
    frank=Duck(20)
    print(frank)
    frank.quack()
    frank.walk()
    
if __name__=="__main__":main()

'''
<__main__.Duck instance at 0x0000000002452688>
('quack quack', 10)
('duck likes a walk', 10)


<__main__.Duck instance at 0x0000000002452388>
('quack quack', 20)
('duck likes a walk', 20)
'''
    