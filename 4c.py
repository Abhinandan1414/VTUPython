"""
Taken from url = https://github.com/TheAlgorithms/Python.git

MIT License

This is a pure Python implementation of the merge sort algorithm

"""
import random
def merge_sort(collection):
  
    def merge(left, right):
        
        result = []
        while left and right:
            
            result.append((left if left[0] <= right[0] else right).pop(0))
        return result + left + right

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))


def function_main():
    
    
    unsorted = random.sample(range(0, 50), 50)
    print("Unsorted: ",unsorted)
    sorted_list = merge_sort(unsorted)
    print("Sorted: ",sorted_list)
    #print(merge_sort(unsorted), sep=",")
    
function_main()