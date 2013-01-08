'''
Created on Aug 31, 2012

@author: Joseph Lee
'''

#pseudocode reference from www.algorithmist.com
def quicksort(array):
    low = 0
    high = len(array)
    if low < high:
        pivot = _partition(array, low, high)
        _quicksort(array, low, pivot - 1)
        _quicksort(array, pivot + 1, high)

def _quicksort(array, low, high):
    if low < high:
        pivot = _partition(array, low, high)
        _quicksort(array, low, pivot - 1)
        _quicksort(array, pivot + 1, high)

def _swap_value(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    
def _partition(array, low, high):
    pivot = array[low]
    left = low
    
    for i in range(low+1, high):
        if(array[i] < pivot):
            left += 1
            _swap_value(array, i, left)
            
    _swap_value(array, low, left)
        
    return left  

#pseudocode reference from en.wikipedia.org/wiki/bubblesort
def bubblesort(array):
    swapped = True
    while swapped:
        swapped = False;
        for i in range(1, len(array)):
            if array[i-1] > array[i]:
                _swap_value(array, i-1, i)
                swapped = True
                
#Roll My Own Sort
def hi_low_sort(array):
    start = 0
    stop = len(array) - 1
    if(start >= stop):
        return;
  
    low = start
    high = stop
    for i in range(start, stop + 1):
        if array[i] < array[low]:
            low = i
        elif array[i] > array[high]:
            high = i
    _swap_value(array, high, stop)        
    _swap_value(array, low, start)
    _hi_low_sort(array, start+1, stop-1)

def _hi_low_sort(array, start, stop):
    if(start >= stop):
        return;
  
    low = start
    high = stop
    for i in range(start, stop + 1):
        if array[i] < array[low]:
            low = i
        elif array[i] > array[high]:
            high = i
    _swap_value(array, high, stop)        
    _swap_value(array, low, start)
    _hi_low_sort(array, start+1, stop-1)
        
    
            
            
            
            
                