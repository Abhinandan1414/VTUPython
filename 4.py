comparison = 0
swaps = 0

comparison1 = 0
swaps1 = 0

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



def insertion_sort_improve(nlist):
    global comparison1
    global swaps1
    for index in range(1,len(nlist)):
        currentvalue = nlist[index]
        position = index

        while position>0 and nlist[position-1]>currentvalue:
            comparison1+= 1
            nlist[position]=nlist[position-1]
            position = position-1
        swaps1+= 1
        nlist[position]=currentvalue
    print(comparison1,"Comparisons and", swaps1, "Swaps")
    return

data = [14,46,43,27,57,41,45,21,70]
data1 = [14,46,43,27,57,41,45,21,70]
insertion_sort_old(data)
print('Sorted Array in Ascending Order:')
print(data)
insertion_sort_improve(data1)
print('Sorted Array in Ascending Order:')
print(data1)