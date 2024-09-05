# Write a Python program to read first n lines of a file. 
# Python program to read the first n lines of a file

def read_first_n_lines(file_name, n):
    with open(file_name, "r") as file:
        # Loop to read the first n lines
        for i in range(n):
            line = file.readline()  # Read one line at a time
            if line == '':  # If the file has fewer than n lines, break early
                break
            print(line, end='')  # Print the line without adding extra newline

# Specify the file name and the number of lines to read
file_name = "example.txt"
n = 3  # Change this to the number of lines you want to read

# Call the function to read the first n lines
read_first_n_lines(file_name, n)
