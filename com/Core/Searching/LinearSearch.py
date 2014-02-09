'''
Created on Feb 8, 2014

@author: Savani Bharat
'''
number_list = [7, 6, 3, 8, 7, 5, 6, 4, 3, 7, 5, 5, 9]
# Linear search
i = 0
while i < len(number_list) and number_list[i] != 9:
    i += 1
     
if i < len(number_list):
    print( "The number is at position", i)
else:
    print( "The number was not in the list." )


'''
('The number is at position', 12)
'''