'''
Created on Feb 8, 2014

@author: Savani Bharat
'''

def binary_search(number_list, key, lower_bound, upper_bound):
    if (upper_bound < lower_bound):
        return None
    else:
        middle_position = lower_bound + ((upper_bound - lower_bound) / 2)
        if number_list[middle_position] > key:
            return binary_search(number_list, key, lower_bound, middle_position-1)
        elif number_list[middle_position] < key:
            return binary_search(number_list, key, middle_position+1, upper_bound)
        else:
            return middle_position
        

if __name__ == "__main__":
    number_list = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]
    lower_bound = 0
    key=8
    upper_bound = len(number_list)-1
    #for key in  [8, 6, 1, 12, 7]:
    index = binary_search(number_list, key, lower_bound, upper_bound)
    print key, index