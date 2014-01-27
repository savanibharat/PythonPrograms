'''
Created on Jan 26, 2014

@author: Savani Bharat
'''


def recursive_factorial(number):
    if number <= 1:
        return 1
    else:
        return number * recursive_factorial(number - 1)
    
input_val = input("enter the number")
factorial = recursive_factorial(input_val)
print factorial
