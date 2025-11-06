# Exception and error handling in Python allows programs to manage unexpected
# situations without crashing. By using try–except blocks, you can catch and
# respond to runtime errors gracefully, provide meaningful messages, maintain
# program flow, and ensure cleanup actions with finally. This makes your code
# more robust, reliable, and user-friendly.

def test():
    pass


#--------------Exxception and error handling in Python----------------#
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed." # Handle division by zero error
    except TypeError:
        return "Error: Invalid input type. Please provide numbers." # Handle non-numeric inputs
    else:
        return result
    finally:
        print("Execution of divide_numbers function is complete.")  # This block always executes
        
if __name__ == "__main__":
    print(divide_numbers(10, 2))  # Valid division
    print(divide_numbers(10, 0))  # Division by zero
    print(divide_numbers(10, 'a'))  # Invalid input type
    
    print("***********************************\n")
    #------------Raising Exceptions------------#
    
user_input = input("Enter a number to check exceptions: ")
n = int(user_input)
if n < 0:
    raise ValueError("Negative value error: n must be non-negative.")  # Raise ValueError for negative n
elif n == 0:
    raise ZeroDivisionError("Zero value error: n must be greater than zero.")  # Raise ZeroDivisionError for zero n
else:
    print(f"The value of n is: {n}")  # Print n if it's valid 

    print("***********************************\n")
#------------Asserting Conditions------------#
def calculate_square_root(x):
    assert x >= 0, "Input must be non-negative."  # Assert that x is non-negative
    return x ** 0.5 
if __name__ == "__main__":
    try:
        print(calculate_square_root(16))  # Valid input
        print(calculate_square_root(-4))  # Invalid input, will raise AssertionError
    except AssertionError as e:
        print(f"Assertion Error: {e}")  # Handle the assertion error           

if (__name__ == "__main__"): # Checking if the script is run directly
        print("Executing as the main module")
        test()
else:
        print("Imported as a module") 