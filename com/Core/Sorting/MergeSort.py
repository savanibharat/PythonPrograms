'''
Created on Jan 27, 2014

@author: Savani Bharat
'''

def merge_sort(list2):
    merge_sort_recursive(list2, 0, len(list2) - 1)

def merge_sort_recursive(list2, first, last):
    if first < last:
        split = (first + last) / 2
        merge_sort_recursive(list2, first, split)
        merge_sort_recursive(list2, split + 1, last)
        merge(list2, first, last, split)
        
def merge(list2, first, last, split):
    helper_list = []
    i = first
    j = split + 1
    while i <= split and j <= last:
        if list2[i] <= list2[j]:
            helper_list.append(list2[i])
            i=i+1
        else:   
            helper_list.append(list2[j])
            j=j+1
    while i <= split:
        helper_list.append(list2[i])
        i = i + 1
    while j <= last:
        helper_list.append(list2[j])
        j = j + 1
        
    for i in range(0,last-first+1):
        list2[first+i]=helper_list[i]
        
        
list=[9,8,7,6,5,4,3,2,1]
merge_sort(list)
print list
