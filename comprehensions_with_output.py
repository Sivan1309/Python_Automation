
# Comprehensions in Python provide a concise and expressive way to create new
# lists, sets, dictionaries, or generators from existing iterables. They allow
# you to combine iteration, filtering, and transformation into a single, readable
# line of code. Comprehensions make data processing faster to write, easier to
# understand, and more efficient compared to traditional loops.


def test():

#----------------Comprehensions in Python----------------#
# List Comprehension
    squares = [x**2 for x in range(10)]
    print("List Comprehension - Squares of numbers from 0 to 9:")
    print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    list_of_strings = ["apple", "banana", "cherry"]
    uppercase_strings = [s.upper() for s in list_of_strings]
    print("List Comprehension - Uppercase strings:")
    print(uppercase_strings)  # Output: ['APPLE', 'BANANA', 'CHERRY']     
    # Dictionary Comprehension
    original_dict = {'a': 1, 'b': 2, 'c': 3}
    squared_dict = {k: v**2 for k, v in original_dict.items()}
    print("Dictionary Comprehension - Squared values:")
    print(squared_dict)  # Output: {'a': 1, 'b': 4, 'c': 9}
    # Set Comprehension
    numbers = [1, 2, 2, 3, 4, 4, 5]
    unique_squares = {x**2 for x in numbers}       
    print("Set Comprehension - Unique squares:")
    print(unique_squares)  # Output: {1, 4, 9, 16, 25}
    # Generator Comprehension
    gen = (x**2 for x in range(5))
    print("Generator Comprehension - Squares of numbers from 0 to 4:")
    for value in gen:
        print(value)  # Output: 0, 1, 4, 9, 16 (each on a new line)   
        
        
if (__name__ == "__main__"): # Checking if the script is run directly
            print("Executing as the main module")
            test()
else:
            print("Imported as a module") 

# ---- OUTPUT ----
Imported as a module
List Comprehension - Squares of numbers from 0 to 9:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
List Comprehension - Uppercase strings:
['APPLE', 'BANANA', 'CHERRY']
Dictionary Comprehension - Squared values:
{'a': 1, 'b': 4, 'c': 9}
Set Comprehension - Unique squares:
{1, 4, 9, 16, 25}
Generator Comprehension - Squares of numbers from 0 to 4:
0
1
4
9
16
