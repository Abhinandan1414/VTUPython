def count_occurrences_of_given_word(file_to_be_searched, passed_word):
    passed_word_count = 0
    # Open the file in read mode
    text = open(file_to_be_searched, "r")

    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Split the line into words
        words = line.split(" ")
                            

        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            if word == passed_word:
                # Increment count of word by 1
                passed_word_count+=1
    print("Given word",passed_word,"occurrences is",passed_word_count)
		
def file_read_desired_lines(file_to_be_searched, line_count_desired):
    f = open(file_to_be_searched, "r")
    print("First" ,line_count_desired,"lines are as follows")
    for i in range(line_count_desired):
        print(f.readline())

def function_main():
    file_to_be_searched = input("Enter the file to be searched")
    word_to_be_searched = input("Enter the word to be searched")
    desired_line_count = int(input("How many lines to be printed"))
    count_occurrences_of_given_word(file_to_be_searched,word_to_be_searched)
    file_read_desired_lines(file_to_be_searched,desired_line_count)

function_main()
