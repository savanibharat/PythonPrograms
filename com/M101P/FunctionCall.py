'''
Created on Feb 4, 2014

@author: Savani Bharat
'''
fruits = ['apple', 'grape', 'apple', 'pear', 'orange', 'grape']

def analyzeList(l):
    counts = {}
    for item in l:
        if item in counts:
            counts[item]=counts[item]+1
        else:
            counts[item]=1
        
    return counts
        
    
    
counts = analyzeList(fruits)
print counts
    
'''
{'orange': 1, 'pear': 1, 'grape': 2, 'apple': 2}
'''