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


# Courtesy https://www.programiz.com/dsa/insertion-sort
def insertion_sort_improve(nlist):
    global comparison1
    global swaps1
    for index in range(1,len(nlist)):
        currentvalue = nlist[index]
        position = index
        while position>0 and nlist[position-1]>currentvalue:
            comparison1+= 1
            nlist[position]=nlist[position-1]
            swaps1+= 1
            position = position-1
        nlist[position]=currentvalue
    print(comparison1,"Comparisons and", swaps1, "Swaps")
    return

# Courtesy https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-8.php
def merge_sort(nlist):
    print("Splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",nlist)

# data = [14,46,43,27,57,41,45,21,70]
# data1 = [14,46,43,27,57,41,45,21,70]
# data2 = [14,46,43,27,57,41,45,21,70]
randomlist = random.sample(range(0, 50), 50)
data = randomlist.copy()
data1 = randomlist.copy()
data2 = randomlist.copy()

insertion_sort_old(data)
print('Sorted Array in Ascending Order:')
print(data)
insertion_sort_improve(data1)
print('Sorted Array in Ascending Order:')
print(data1)
merge_sort(data2)
print('Sorted Array in Ascending Order:')
print(data2)
