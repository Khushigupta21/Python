# Python program to copy the contents of one file to another file

def copy_file_contents(source_file, destination_file):
    with open(source_file, "r") as src_file:
        content = src_file.read()  # Read the entire content of the source file
    
    with open(destination_file, "w") as dest_file:
        dest_file.write(content)  # Write the content to the destination file

# Specify the source and destination file names
source_file = "source.txt"
destination_file = "destination.txt"

# Call the function to copy contents
copy_file_contents(source_file, destination_file)

print(f"Contents of {source_file} have been copied to {destination_file}.")
