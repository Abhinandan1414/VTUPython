def count_occurrences_of_digits(num):
    dictionary = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
    temp = num
    while(temp > 0):
        dig=temp % 10
        dictionary[dig] = dictionary[dig] + 1
        temp = temp//10
    return dictionary

def is_palindrome(num):
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        return True
    else:
        return False

def function_main():
    digits_in_decimal = 10
    num=int(input("Enter number:"))
    num_is_palindrome = is_palindrome(num)
    if(num_is_palindrome):
        print("It is a palindrome")
    else:
        print("It is NOT a palindrome")
    retuned_dictionary = count_occurrences_of_digits(num)
    for i in range(digits_in_decimal):
        print(i,"Occured",retuned_dictionary[i],"times")

function_main()