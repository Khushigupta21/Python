# Write a Python program to count the number of lines in a text file. 
# Python program to count the number of lines in a file

def count_lines(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()  # Read all lines
    return len(lines)  # Return the total number of lines

# Specify the file name
file_name = "example.txt"

# Call the function to count lines
line_count = count_lines(file_name)

# Print the number of lines
print(f"The file has {line_count} lines.")
