'''
Created on Aug 31, 2012

@author: Joseph Lee
'''
import random
import time
from sort import quicksort, bubblesort, hi_low_sort

def create_list():
    ran = random
    a = []
    for i in range(1000):
        a.append(ran.randint(1, 1000000))
    return a

def print_list(a):
    for i in range(0, len(a), 10):
        print(a[i], a[i+1], a[i+2], a[i+3], a[i+4],
               a[i+5], a[i+6], a[i+7], a[i+8], a[i+9])
        
def main():
    a = create_list()
    start = time.time()
    quicksort(a)
    elapsed = (time.time() - start)
    print_list(a)
    print("--Quick Sort--")
    print("Total Sort Time: ", elapsed)
    print()
    input("press enter to run next sort")
    
    a = create_list()
    start = time.time()
    bubblesort(a)
    elapsed = (time.time() - start)
    print_list(a)
    print("--Bubble Sort--")
    print("Total Sort Time: ", elapsed)
    print()
    input("press enter to run next sort")
    
    a = create_list()
    start = time.time()
    hi_low_sort(a)
    elapsed = (time.time() - start)
    print_list(a)
    print("--hi_low Sort--")
    print("Total Sort Time: ", elapsed)
    input("press enter to end")

if __name__ == '__main__':
    main()