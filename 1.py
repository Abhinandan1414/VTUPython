'''
1.a
Write a python program to find the best of two test average marks out of three test’s
marks accepted from the user.
'''

def list_avg(test_marks):
    return sum(test_marks)/ len(test_marks)

def give_best_two(test_marks):
    return_list = []
    test_marks.sort(reverse=True)
    return_list.append(test_marks[0])
    return_list.append(test_marks[1])
    return return_list

def function_main():
    passed_list = []
    return_list = []
    first_test_marks = int(input('Enter the first test marks'))
    second_test_marks = int(input('Enter the second test marks'))
    third_test_marks = int(input('Enter the third test marks'))
    passed_list.append(first_test_marks)
    passed_list.append(second_test_marks)
    passed_list.append(third_test_marks)
    return_list = give_best_two(passed_list)
    avg_of_best_two = list_avg(return_list)
    print("You passed marks :",first_test_marks,",",second_test_marks,",",third_test_marks,"")
    print("Best two",return_list)
    print("Average of best two tests is",avg_of_best_two)

if __name__=='__main__':
    print(__doc__)
    function_main()

