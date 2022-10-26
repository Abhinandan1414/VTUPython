''' 
8.
 Write a python program to find the whether the given input is palindrome or not (for
both string and integer) using the concept of polymorphism and inheritance.
'''
import math

class number:

    def __init__(self):
        self.stored_value = 0
    
    def check_palindrome(self):
        pass
        
    
class palindrome(number):

    def __init__(self, passed_number):
        self.stored_value= passed_number
       

    def check_palindrome(self):
        num=self.stored_value
        rev=0
        while(num>0):
            dig=num%10
            rev=rev*10+dig
            num=num//10
        if(self.stored_value==rev):
            print("It is palindrome")
        else:
            print("It is not palindrome")

class palindrome_string_input(number):

    def __init__(self,passed_string):
        self.stored_value = passed_string

    def check_palindrome(self):
        num=int(self.stored_value)
        rev=0
        while(num>0):
            dig=num%10
            rev=rev*10+dig
            num=num//10
        if(int(self.stored_value)==rev):
            print("It is palindrome")
        else:
            print("It is not palindrome")



def function_main():
    base_num = number()
    test_num = palindrome(12121)
    base_num = test_num
    base_num.check_palindrome()
    test_num1 = palindrome(12122)
    base_num = test_num1
    base_num.check_palindrome()
    string_num = palindrome_string_input("12121")
    base_num = string_num
    base_num.check_palindrome()
    string_num1 = palindrome_string_input("12131")
    base_num = string_num1
    base_num.check_palindrome()

if __name__=='__main__':
    print(__doc__)   
    function_main()


