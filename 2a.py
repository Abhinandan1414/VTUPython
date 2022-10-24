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


main_function()
