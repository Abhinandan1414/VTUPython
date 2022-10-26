'''
6.a
Write a python program to accept a file name from the user and perform the following
operations
1. Display the first N line of the file
2. Find the frequency of occurrence of the word accepted from the user in the
file
'''


def count_occurrences_of_given_word(file_to_be_searched, passed_word):
    passed_word_count = 0
   
    text = open(file_to_be_searched, "r")

   
    for line in text:
        line = line.strip()
        words = line.split(" ")
 
        for word in words:
            
            if word == passed_word:
                
                passed_word_count+=1
    print("Given word",passed_word,"occurrences is",passed_word_count)
		
def file_read_desired_lines(file_to_be_searched, line_count_desired):
    f = open(file_to_be_searched, "r")
    print("First" ,line_count_desired,"lines are as follows")
    for i in range(line_count_desired):
        print(f.readline())

def function_main():
    file_to_be_searched = input("Enter the file to be searched: ")
    word_to_be_searched = input("Enter the word to be searched: ")
    desired_line_count = int(input("How many lines to be printed: "))
    count_occurrences_of_given_word(file_to_be_searched,word_to_be_searched)
    file_read_desired_lines(file_to_be_searched,desired_line_count)
    
if __name__=='__main__':
    function_main()
