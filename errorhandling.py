def get_valid_number(prompt):
    """
    Get a valid number from user input with error handling.
    
    Args:
        prompt (str): The prompt message to display
        
    Returns:
        float: A valid number entered by the user
    """
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Error: Please enter a valid number!")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            exit()

def get_non_zero_divisor():
    """
    Get a valid non-zero number for division.
    
    Returns:
        float: A valid non-zero number
    """
    while True:
        try:
            divisor = float(input("Enter the second number (divisor): "))
            if divisor == 0:
                print("Error: Cannot divide by zero! Please enter a non-zero number.")
                continue
            return divisor
        except ValueError:
            print("Error: Please enter a valid number!")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            exit()

def main():
    """
    Main function to handle the division operation with error handling.
    """
    print("=== Division Calculator with Error Handling ===")
    print("Enter 'quit' or press Ctrl+C to exit the program.\n")
    
    while True:
        try:
        
            user_input = input("Do you want to perform division? (y/n or 'quit' to exit): ").lower().strip()
            
            if user_input in ['quit', 'exit', 'q']:
                print("Thank you for using the calculator. Goodbye!")
                break
            elif user_input in ['n', 'no']:
                print("Thank you for using the calculator. Goodbye!")
                break
            elif user_input not in ['y', 'yes', '']:
                print("Please enter 'y' for yes, 'n' for no, or 'quit' to exit.")
                continue
            
            
            dividend = get_valid_number("Enter the first number (dividend): ")
            
        
            divisor = get_non_zero_divisor()
            
            
            result = dividend / divisor
            
            
            print(f"\nResult: {dividend} ÷ {divisor} = {result}")
            print(f"Formatted result: {result:.4f}")
            print("-" * 40)
            
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()