# Q:5 Write a Python program to read last n lines of a file. 

def read_last_n_lines(file_name, n):
    with open(file_name, "r") as file:
        lines = file.readlines()  # Read all lines of the file into a list
        last_n_lines = lines[-n:]  # Get the last n lines
        for line in last_n_lines:
            print(line, end='')  # Print each line without adding extra newline

# Specify the file name and the number of lines to read
file_name = "example.txt"
n = 5  # Change this to the number of lines you want to read

# Call the function to read the last n lines
read_last_n_lines(file_name, n)
