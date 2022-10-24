"""
Taken from url = https://github.com/TheAlgorithms/Python.git

This is a pure Python implementation of the merge sort algorithm

"""
import time


def merge_sort(collection):
  
    def merge(left, right):
        #print("merge is called")
        result = []
        while left and right:
            #print("Element is being added to the sorted list")
            result.append((left if left[0] <= right[0] else right).pop(0))
        return result + left + right

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))


def function_main():
    start = time.time()
    unsorted = [14,46,43,27,57,41,45,21,70]
    print(merge_sort(unsorted), sep=",")
    end = time.time()
    print("Execution time is",(end-start) * 10**3, "ms")

function_main()