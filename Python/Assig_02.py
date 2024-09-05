# Q:2 Write a Python program to read an entire text file.

file = open("example.txt", "r")  # Open the file in read mode
content = file.read()            # Read the whole content
print(content)
file.close()
