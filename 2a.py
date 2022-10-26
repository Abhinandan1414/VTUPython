'''
2.a
Defined as a function F as Fn = Fn-1 + Fn-2. Write a Python program which accepts a
value for N (where N >0) as input and pass this value to the function. Display suitable
error message if the condition for input value is not followed.
'''

def nth_term_of_fibonnaci(n):
   if n <= 1:
       return n
   else:
       return(nth_term_of_fibonnaci(n-1) + nth_term_of_fibonnaci(n-2))


def main_function():
    nterms = int(input("Enter number of terms of Fibonacci "))
    if nterms <= 0:
        print("Plese enter a positive integer")
    else:
        print("Fibonacci sequence:")
    for i in range(nterms):
       print(nth_term_of_fibonnaci(i), end=' ')

if __name__=='__main__':
    print(__doc__)
    main_function()
