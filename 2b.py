'''
2.b
Develop a python program to convert binary to decimal, octal to hexadecimal using
functions
'''
def binary_to_decimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(decimal)   



def octal_to_hex(octal):
    octal1 = octal
    decimal, i, n = 0, 0, 0
    while(octal != 0):
        dec = octal % 10
        decimal = decimal + dec * pow(8, i)
        octal = octal//10
        i += 1
    print(hex(decimal))

    
def function_main():
    entered_binary_value = int(input("Enter the binary value in string format"))
    entered_octal_value = int(input("Enter the octal value in string format"))

    binary_to_decimal(entered_binary_value)
    octal_to_hex(entered_octal_value)
    return

if __name__=='__main__':
    print(__doc__)
    function_main()