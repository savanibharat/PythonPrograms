'''
Created on Jan 27, 2014

@author: Savani Bharat
'''
def bubbleSort(list2):
    print list2
    for i in range(0,len(list2)-1):
        for j in range (0,len(list2)-i-1):
            if list2[j]>list2[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
            print list2
list=[5,4,3,2,1]
bubbleSort(list)
'''
[5, 4, 3, 2, 1]
[4, 5, 3, 2, 1]
[4, 3, 5, 2, 1]
[4, 3, 2, 5, 1]
[4, 3, 2, 1, 5]
[3, 4, 2, 1, 5]
[3, 2, 4, 1, 5]
[3, 2, 1, 4, 5]
[2, 3, 1, 4, 5]
[2, 1, 3, 4, 5]
[1, 2, 3, 4, 5]

'''