
# The finally block is executed after the try block and any associated except blocks, regardless of whether an exception was raised or not.
# This ensures that the code within the finally block always runs, which is useful for cleanup actions like closing files, releasing resources, or any other necessary final ste

def file_operations():
    try:
        # Simulate file operations
        print("Opening file...")
        # Simulating a file operation that raises an exception
        raise ValueError("An error occurred while processing the file.")
    except ValueError as e:
        print(f"Exception caught: {e}")
    finally:
        # This block will always execute
        print("Closing file...")

# Call the function
file_operations()
