'''
Created on Feb 24, 2014

@author: Savani Bharat
'''
class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs
    
    def quak(self):
        print("quaaaack")
    
    def walk(self):
        print("walks like a duck")
    
    def get_properties(self, key):
        return self.properties
    
    def get_property(self, key):
        return self.properties.get(key, None)
    
    @property
    def color(self):
        return self.properties.get('color', None)
    
    @color.setter
    def color(self, c):
        self.properties['color'] = c
        
    @color.deleter
    def color(self):
        del self.properties['color']
        
def main():
    donald = Duck()
    donald.color('blue')
    print(donald.color)
    
if __name__ == "__main__":main()
