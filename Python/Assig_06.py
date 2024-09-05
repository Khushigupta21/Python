# Write a Python program to read a file line by line and store it into a list  Write a Python program to read a file line by line store it into a variable.

# Python program to read a file line by line and store it into a list

def file_to_list(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()  # Read all lines into a list
    return lines

# Specify the file name
file_name = "example.txt"

# Call the function and store the lines in a list
lines_list = file_to_list(file_name)

# Print the list of lines
print(lines_list)



# Python program to read a file line by line and store it into a variable

def file_to_variable(file_name):
    with open(file_name, "r") as file:
        content = file.read()  # Read the entire file content
    return content

# Specify the file name
file_name = "example.txt"

# Call the function and store the content in a variable
file_content = file_to_variable(file_name)

# Print the file content
print(file_content)
