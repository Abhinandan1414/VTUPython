def count_occurrences_of_given_word(passed_word):
    passed_word_count = 0
    # Open the file in read mode
    text = open("sample.txt", "r")

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
    print("Given word occurrences is",passed_word_count)
		
def file_read_desired_lines(line_count_desired):
    f = open("sample.txt", "r")
    for i in range(line_count_desired):
        print(f.readline())

def function_main():
    count_occurrences_of_given_word("Hi")
    file_read_desired_lines(4)

function_main()
