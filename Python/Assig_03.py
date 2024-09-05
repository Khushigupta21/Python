#Write a Python program to append text to a file and display the text. 

with open("example.txt", "a") as file:
    file.write("\nThis line is appended to the file.")
