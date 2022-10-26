'''
4.a
Write a python program to implement insertion sort and merge sort using lists
'''

import time
import random
comparison,swaps,comparison1,swaps1 = 0,0,0,0

# Nearly Brute Force
def insertion_sort_old(unsorted_list):
    global comparison
    global swaps
    for i in range(len(unsorted_list)):
        j = i + 1
        for j in range(len(unsorted_list)):
            comparison+=1
            if unsorted_list[i] < unsorted_list[j]:
                swaps+= 1
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[j]
                unsorted_list[j] = temp
    print(comparison,"Comparisons and", swaps, "Swaps")
    return




randomlist = random.sample(range(0, 50), 50)
data = randomlist.copy()
data1 = randomlist.copy()
data2 = randomlist.copy()

insertion_sort_old(data)
print('Sorted Array in Ascending Order:')
print(data)
