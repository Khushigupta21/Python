# Q:14 How many except statements can a try-except block have? Name Some built-in exception classes: When will the else part of try-except-else be executed?
try:
    # Code that might raise exceptions
    pass
except ValueError:
    # Handle ValueError
    pass
except TypeError:
    # Handle TypeError
    pass
except (IndexError, KeyError):
    # Handle both IndexError and KeyError
    pass
