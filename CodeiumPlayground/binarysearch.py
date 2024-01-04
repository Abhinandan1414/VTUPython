def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# test code
test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_target = 5
result = binary_search(test_array, test_target)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
