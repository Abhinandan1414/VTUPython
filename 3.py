from difflib import SequenceMatcher

def similarity_ratio_between_two_strings(string1,string2):
    print("Entered Strings are:",string1,"and:",string2)
    print("Similarity ratio between two strings :", end="")
    print(SequenceMatcher(None, string1, string2).ratio())
    return

def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0,"DIGITS":0,"WORDCOUNT":0}

    upper_case = []
    lower_case = []
    digits = []

    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
           upper_case.append(c)
        elif c.islower():
           d["LOWER_CASE"]+=1
           lower_case.append(c)
        elif c.isdigit():
            d["DIGITS"]+=1
            digits.append(c)
        elif c.isspace():
            d["WORDCOUNT"]+=1
        else:
           pass
    print ("Entered String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])
    print ("No. of digits :", d["DIGITS"])
    print ("No. of words : ", d["WORDCOUNT"]+1)   
    print("Upper case characters",upper_case)
    print("Lower case characters",lower_case)
    print("DIGITS characters",digits)
    return

def main_function():
    print("===== Menu ===========")
    print("1. String Statistics")
    print("2. String Similarity")
    print("Enter 1 or 2")
    print("===========================")
    choice = int(input())
    if choice != 1 and choice != 2:
        print("Please enter 1 or 2 only")
    if choice == 1:
        input_str = input("Enter the input string whos statistics you want")
        string_test(input_str)
    elif choice == 2:
        string1 = input("Enter the first string")
        string2 = input("Enter the second string")
        similarity_ratio_between_two_strings(string1,string2)
    return

    

main_function()