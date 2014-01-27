'''
Created on Jan 27, 2014

@author: Savani Bharat
'''
def quickSort(list2):
    quickSortRecursive(list2, 0, len(list) - 1)

def quickSortRecursive(list2, first, last):
    if last > first:
        pivot = partition(list2, first, last)
        quickSortRecursive(list2, first, pivot-1)
        quickSortRecursive(list2, pivot + 1, last)

def partition(list2, first, last):
    split = (first + last) / 2
    
    if(list2[first] > list2[split]):#swap first and pivot if pivot is small
        list2[first], list2[split] = list2[split], list2[first]
    
    if(list2[first]>list2[last]):#swap first and last if last is small
        list2[first],list2[last]=list2[last],list[first]
    
    if list2[split]>list2[last]:#swap pivot and last if pivot is small than last
        list2[split],list2[last]=list2[last],list2[split]

    list2[split],list2[first]=list2[first],list2[split]
    
    '''
    f s l
    5 4 3 
1)  4 5 3  5>4
2)  3 5 4  4>3
3)  3 4 5  5>4
    
    '''
    
    pivot=first
    i=first+1
    j=last
    
    while True:
        while  i<=last and list2[i]<=list2[pivot] :
            i=i+1
        while j>=first and list2[j]>list2[pivot] :
            j=j-1      
        if i>=j:
            break
        else:
            list2[j],list2[i]=list2[i],list2[j]
        
    list2[j],list2[pivot]=list2[pivot],list2[j]
    return j

list=[6,5,4,3,2,1]
quickSort(list)
print list

