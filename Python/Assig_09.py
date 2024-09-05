# Python program to count the frequency of words in a file

from collections import Counter
import string

def count_word_frequency(file_name):
    with open(file_name, "r") as file:
        text = file.read().lower()  # Read the file content and convert to lowercase
        text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
        words = text.split()  # Split the text into words
    word_count = Counter(words)  # Use Counter to count the frequency of each word
    return word_count

# Specify the file name
file_name = "example.txt"

# Call the function to count word frequency
word_frequencies = count_word_frequency(file_name)

# Print the word frequencies
for word, count in word_frequencies.items():
    print(f"'{word}': {count} time(s)")
