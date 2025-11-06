# A tuple is an ordered, immutable collection in Python that can store multiple items.
# Once created, its elements cannot be changed, making it useful for fixed or constant data.


def test():
    # -------------tuples-------------
    tuple_example = (1, "two", 3.0, True, (5, 6), [7, 8], {"nine": 9})
    print(tuple_example)
    print(tuple_example[1] * 3)  # Accessing and repeating an element
    print(tuple_example[4])  # Accessing a nested tuple
    print(tuple_example[5])  # Accessing a nested list
    print(tuple_example[6])  # Accessing a nested dictionary
    print(len(tuple_example))  # Length of the tuple
    print(2 in tuple_example)  # Membership test
    print("two" in tuple_example)  # Membership test
    print(tuple_example.count(3.0))  # Counting occurrences of an element
    print(tuple_example.index(True))  # Finding index of an element , here index(True) acts as == so it returns first index as the value is '1' which is equivalent to True
    idx = next((i for i,x in enumerate(tuple_example) if x is True), None) #Using generated expression to find index of True 
    print(idx) 
    # tuple_example[0] = 100  # Attempting to modify an element (will raise an error)
    # tuple_example.append("new_item")  # Attempting to add an element (will raise an error)
    # tuple_example.remove(3.0)  # Attempting to remove an element (will raise an error)
    tuple_example[5].append(9)  # Modifying a mutable element within the tuple
    print(tuple_example)
    
if (__name__ == "__main__"): # Checking if the script is run directly
        print("Executing as the main module")
        test()
else:
        print("Imported as a module") 

# ---- OUTPUT ----
Imported as a module
(1, 'two', 3.0, True, (5, 6), [7, 8], {'nine': 9})
twotwotwo
(5, 6)
[7, 8]
{'nine': 9}
7
False
True
1
0
3
(1, 'two', 3.0, True, (5, 6), [7, 8, 9], {'nine': 9})
