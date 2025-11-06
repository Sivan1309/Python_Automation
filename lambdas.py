# Lambda functions in Python are small, anonymous functions defined using the
# 'lambda' keyword. They are typically used for short, one-line operations where
# a full function definition would be unnecessary. Lambda functions can take any
# number of arguments but contain only a single expression, making them useful
# for quick data transformations, sorting, filtering, and as inline callbacks in
# functions like map(), filter(), and sorted(). They help write concise and
# readable code for simple functional operations.

def test():
    pass

    #---------------lambda functions------------------#
    add = lambda a, b: a + b
    subtract = lambda a, b: a - b
    multiply = lambda a, b: a * b
    divide = lambda a, b: "Error! Division by zero." if b == 0 else a / b
    power = lambda a, b: a ** b
    modulus = lambda a, b: a % b
    floor_divide = lambda a, b: "Error! Division by zero." if b == 0 else a // b
    #---------------------------------------------------#
    def calculate(operation, a, b): # Function to perform calculation based on operation
        operations = {
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide,
            'power': power,
            'modulus': modulus,
            'floor_divide': floor_divide
        }
        if operation in operations: # Check if operation is valid
            return operations[operation](a, b) # Call the corresponding lambda function
        else:
            return "Error! Invalid operation."
    #-----------------------------------------#
    # Getting user input for dynamic calculations
    if __name__ == "__main__":
        operation = input("Enter operation (add, subtract, multiply, divide, power, modulus, floor_divide): ")
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = calculate(operation, a, b)
        print(f"The result of {operation} between {a} and {b} is: {result}")    

    blocks = lambda x,y: x // y if y != 0 else "Error! Division by zero." # Example usage of blocks lambda function
    if __name__ == "__main__":
        print(blocks(10, 3))  # Output: 3
        print(blocks(10, 0))  # Output: Error! Division by zero.        
        
if (__name__ == "__main__"): # Checking if the script is run directly
            print("Executing as the main module")
            test()
else:
            print("Imported as a module") 