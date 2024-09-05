#Q:1 What is File function in python? What is keywords to create and write file.

file = open("example.txt", "w")  # Creates a file if not present, and opens it in write mode
file.write("Hello, world!")      # Writes data to the file
file.close()                     # Closes the file to free up resources

# "r" (read): Opens the file for reading. It throws an error if the file doesn't exist.
# "w" (write): Opens the file for writing. If the file exists, it is overwritten. If not, it's created.
# "a" (append): Opens the file for appending data. New data will be added at the end of the file. It creates the file if it doesn’t exist.
# "x" (exclusive creation): Creates a new file. If the file exists, it raises a FileExistsError.
# "b" (binary): Opens the file in binary mode (useful for images or non-text files).
# "t" (text): Opens the file in text mode (default mode for most operations)