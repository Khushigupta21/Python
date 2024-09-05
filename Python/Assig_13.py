# Explain Exception handling? What is an Error in Python?

# Ans : Exception Handling allows for graceful error management and recovery in Python.
#     Errors are categorized into syntax errors (detected by the interpreter before execution) and exceptions (occur during execution).

try:
    num = int(input("Enter a number: "))  # This can raise ValueError
    result = 10 / num  # This can raise ZeroDivisionError
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
