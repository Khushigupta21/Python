# Write a python program to find the longest words. 

def find_longest_words(file_name):
    with open(file_name, "r") as file:
        words = file.read().split()  # Read the file and split into words
    max_len = len(max(words, key=len))  # Find the length of the longest word(s)
    longest_words = [word for word in words if len(word) == max_len]  # Collect all words with max length
    return longest_words

# Specify the file name
file_name = "example.txt"

# Call the function to find the longest word(s)
longest_words = find_longest_words(file_name)

# Print the longest word(s)
print("The longest word(s):", longest_words)
