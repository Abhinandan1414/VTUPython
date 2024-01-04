def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_list = merge_sort(lst[:mid])
    right_list = merge_sort(lst[mid:])

    return merge(left_list, right_list)


def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        sorted_list.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        sorted_list.append(right[right_index])
        right_index += 1

    return sorted_list
def test_merge_sort():
    data = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    result = merge_sort(data)
    assert result == [6, 8, 19, 20, 23, 41, 49, 53, 56, 87], 'Test Failed'

    data = []
    result = merge_sort(data)
    assert result == [], 'Test Failed'

    data = [6]
    result = merge_sort(data)
    assert result == [6], 'Test Failed'

    print('All test cases pass')
    
if __name__ == '__main__':
    test_merge_sort()
