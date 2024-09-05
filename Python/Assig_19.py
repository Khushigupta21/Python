#Write python program that user to enter only odd numbers, else will raise an exception
def get_odd_number():
    while True:
        try:
            # Prompt the user to enter a number
            user_input = int(input("Enter an odd number: "))
            
            # Check if the number is odd
            if user_input % 2 == 0:
                # Raise an exception if the number is even
                raise ValueError("The number entered is not odd.")
            
            # If the number is odd, break out of the loop
            print(f"Thank you! You entered the odd number: {user_input}")
            break
        
        except ValueError as ve:
            # Handle invalid input or non-odd number
            print(f"Error: {ve}. Please try again.")
        
        except Exception as e:
            # Handle other unexpected exceptions
            print(f"Unexpected error: {e}. Please try again.")

# Call the function to execute
get_odd_number()
