'''
Created on Jan 26, 2014

@author: Savani Bharat
'''

def selection_sort(list2):
    
    for i in range(0,len(list2)):
        min=i
        for j in range(i,len(list2)):
            if list2[min]>list2[j]:
                min=j
            print list2
        list2[i],list2[min]=list2[min],list2[i]
        '''list2[i] will be assigned list2[min] which is on right side of =
        list2[min] will be assigned value list2[i]
        '''
list = [7,6,5,4,3,2,1]
selection_sort(list)
print list

'''
[7, 6, 5, 4, 3, 2, 1]
[7, 6, 5, 4, 3, 2, 1]
[7, 6, 5, 4, 3, 2, 1]
[7, 6, 5, 4, 3, 2, 1]
[7, 6, 5, 4, 3, 2, 1]
[7, 6, 5, 4, 3, 2, 1]
[7, 6, 5, 4, 3, 2, 1]
[1, 6, 5, 4, 3, 2, 7]
[1, 6, 5, 4, 3, 2, 7]
[1, 6, 5, 4, 3, 2, 7]
[1, 6, 5, 4, 3, 2, 7]
[1, 6, 5, 4, 3, 2, 7]
[1, 6, 5, 4, 3, 2, 7]
[1, 2, 5, 4, 3, 6, 7]
[1, 2, 5, 4, 3, 6, 7]
[1, 2, 5, 4, 3, 6, 7]
[1, 2, 5, 4, 3, 6, 7]
[1, 2, 5, 4, 3, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]

'''