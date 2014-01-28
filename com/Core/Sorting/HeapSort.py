'''
Created on Jan 27, 2014

@author: Savani Bharat
'''

def heapSort(list2):
    first = 0
    last = len(list2) - 1
    create_heap(list2, first, last)
  
    for i in range(last, first, -1):
        list2[i], list2[first] = list2[first], list2[i]
        establishHeapProperty(list2, first, i - 1)
        
def create_heap(list2, first, last):
    i = last / 2
    
    while i >= first:
        establishHeapProperty(list2, i, last)
        i = i - 1
        
def establishHeapProperty(list2, first, last):
    
    while 2 * first + 1 <= last:
        k = 2 * first + 1
        
        if k < last and list2[k] < list2[k + 1]:
            k = k + 1
        
        if list2[first] >= list2[k]:
            break
        list2[first], list2[k] = list2[k], list2[first]
        first = k


list=[8,7,6,5,4,3,2,1]
heapSort(list)
print list