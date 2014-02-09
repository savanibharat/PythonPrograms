'''
Created on Feb 8, 2014

@author: Savani Bharat
'''
number_list = [1,2,4,5,12,13,16,17,88,99,177]
key = 17;
lower_bound = 0
upper_bound = len(number_list) - 1;
found = False;
while lower_bound <= upper_bound and not found:
    
    middle_position = (lower_bound + upper_bound) / 2
    
    if number_list[middle_position] < key:
        lower_bound = middle_position + 1
    
    elif number_list[middle_position] > key:
        upper_bound = middle_position - 1
    
    else:
        found = True;
        
if found:
    print ("Number found")
else:
    print("number not found")

'''
Number found
'''