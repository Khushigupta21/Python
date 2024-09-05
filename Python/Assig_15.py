# Can one block of except statements handle multiple exception? 
# Ans: Yes, a single except block can handle multiple exceptions. 
# You can specify multiple exceptions in a single except statement by grouping them in a tuple.
# This allows you to handle different exceptions with the same code.

try:
    # Code that might raise an exception
    num = int(input("Enter a number: "))
    result = 10 / num
except (ValueError, ZeroDivisionError) as e:
    # Handle both ValueError and ZeroDivisionError
    print(f"An error occurred: {e}")
