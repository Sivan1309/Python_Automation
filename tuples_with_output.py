# Tuples are an ordered, immutable sequence type in Python that can hold heterogeneous elements (ints, strings, floats, booleans, other tuples, lists, dicts, etc.). You create them with parentheses or the tuple() constructor; note that a single-element tuple requires a trailing comma (e.g., (42,) ) to distinguish it from a parenthesized expression.

# Because tuples are immutable, you cannot reassign, append, or remove items from the tuple itself. However, immutability applies to the container — if a tuple contains a mutable object (like a list or dict), that contained object can be modified in place, and the change will be visible through the tuple reference.

# Tuples support indexing, slicing, and iteration like lists, and provide a small API: len(), count(), index(), and membership testing with the in operator. Unpacking (a, b = my_tuple) and extended unpacking (a, *rest, z = my_tuple) are common, concise ways to assign tuple contents to variables.

# Common uses for tuples include grouping related but fixed collections of values, returning multiple values from functions, and using tuples as dictionary keys or set elements when their contents are immutable. Tuples are slightly more memory- and lookup-efficient than lists for small, fixed collections.

# Be mindful of equality vs identity with booleans and integers (e.g., 1 == True); index() and count() use equality (==). If you need to locate the actual True object rather than values equal to it, use identity checks (is True) when searching.

# Overall, use tuples when you want an ordered, fixed-size container that signals immutability and can be relied on as a stable value (for keys, return values, or lightweight records).

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
