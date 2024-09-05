# Python program to write a list to a file

def write_list_to_file(file_name, my_list):
    with open(file_name, "w") as file:
        for item in my_list:
            file.write(f"{item}\n")  # Write each item followed by a newline

# Example list
my_list = ["Python", "Java", "C++", "JavaScript", "Ruby"]

# Specify the file name
file_name = "languages.txt"

# Call the function to write the list to the file
write_list_to_file(file_name, my_list)

print(f"The list has been written to {file_name}.")
