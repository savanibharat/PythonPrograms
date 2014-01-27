'''
Created on Jan 19, 2014

@author: Savani Bharat
'''

'''temp = 1
i = input("Enter number for factorial")
while i > 0:
    temp = temp * i
    i = i - 1
print temp
   '''
   
    
def factorial(fact):
    product=1
    for i in range(fact):
        product=product*(i+1)
    return product

user_input=input("enter the number")
user_input_factorial=factorial(user_input)
print user_input_factorial