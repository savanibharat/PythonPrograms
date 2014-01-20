'''
Created on Jan 19, 2014

@author: Savani Bharat
'''
print range(5)

print range(1, 6)  # includes first parameter but not second so output is [Pa,Px,..,P(b-1)] where Pa is first pameter

print range(1, 6, 2)

sum = 0
for i in range(10):
    sum = sum + i
    print sum
    
"""
[0, 1, 2, 3, 4]
[1, 2, 3, 4, 5]
[1, 3, 5]
0
1
3
6
10
15
21
28
36
45
"""