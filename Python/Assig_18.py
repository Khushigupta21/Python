def process_file(file_name):
    try:
        file = open(file_name, "r")
        content = file.read()
        print(content)
    except FileNotFoundError:
        # Handle file not found error
        print(f"Error: The file '{file_name}' does not exist.")
    except IOError:
        # Handle other I/O errors
        print(f"Error: An I/O error occurred while reading the file.")
    finally:
        # Ensure the file is closed even if an error occurs
        try:
            file.close()
        except:
            # Handle potential errors in closing the file
            print("Error: The file could not be closed.")

# Example usage
process_file("example.txt")
