
# A list is an ordered, mutable collection used to store multiple items in Python.
# It allows adding, removing, and modifying elements, and can hold mixed data types.
def test():
    #-------------------Lists-------------
    
    list_example = [10, "twenty", 30.0, False, [40, 50], (60, 70), {"eighty": 80}]
    print(list_example)
    list_example.append("crackjack")  # Adding an element
    print(list_example)
    list_example.pop()  # Removing the last element
    print(list_example)
    list_example.insert(1, "Audi")  # Inserting an element at  index 1
    print(list_example)
    list_example.remove(30.0)  # Removing a specific element
    print(list_example)
    list_example[3] = True  # Modifying an element
    print(list_example)
    print(list_example[4])  # Accessing a nested list
    print(list_example[5])  # Accessing a nested tuple
    print(list_example[6])  # Accessing a nested dictionary
    print(len(list_example))  # Length of the list
    print("twenty" in list_example)  # Membership test
    print(list_example.count(True))  # Counting occurrences of an element
    print(list_example.index("Audi"))  # Finding index of an element
    print(sorted([3,1,4,2]))  # Sorting a list
    print("#########################\n")
    list_example.reverse()  # Reversing the list
    print(list_example)
    list_example_1= list_example[::-1]  # Another way to reverse the list using slicing
    print(list_example_1)
    list_example.extend(list_example_1)  # Extending the list with another list
    print(list_example)
    print("#########################\n")
    list_example=list_example_1
    print(list_example.append("Tom Cruise"))  # Appending an element
    list_example_1=list_example.copy() # Shallow copy of the list
    print(list_example_1)
    list_example[3] = "Changed Value"  # Modifying an element in the original list
    print(list_example)
    print(list_example_1)  # Copied list remains unchanged
    New_list = [item for item in list_example if isinstance(item, int)]  # List comprehension to filter integers
    print(New_list)
    New_list_map = list(map(lambda x: x*2 if isinstance(x, int) else x, list_example))  # Using map to double integers
    print(New_list_map)
    
if (__name__ == "__main__"): # Checking if the script is run directly
        print("Executing as the main module")
        test()
else:
        print("Imported as a module") 

# ---- OUTPUT ----
Imported as a module
[10, 'twenty', 30.0, False, [40, 50], (60, 70), {'eighty': 80}]
[10, 'twenty', 30.0, False, [40, 50], (60, 70), {'eighty': 80}, 'crackjack']
[10, 'twenty', 30.0, False, [40, 50], (60, 70), {'eighty': 80}]
[10, 'Audi', 'twenty', 30.0, False, [40, 50], (60, 70), {'eighty': 80}]
[10, 'Audi', 'twenty', False, [40, 50], (60, 70), {'eighty': 80}]
[10, 'Audi', 'twenty', True, [40, 50], (60, 70), {'eighty': 80}]
[40, 50]
(60, 70)
{'eighty': 80}
7
True
1
1
[1, 2, 3, 4]
#########################

[{'eighty': 80}, (60, 70), [40, 50], True, 'twenty', 'Audi', 10]
[10, 'Audi', 'twenty', True, [40, 50], (60, 70), {'eighty': 80}]
[{'eighty': 80}, (60, 70), [40, 50], True, 'twenty', 'Audi', 10, 10, 'Audi', 'twenty', True, [40, 50], (60, 70), {'eighty': 80}]
#########################

None
[10, 'Audi', 'twenty', True, [40, 50], (60, 70), {'eighty': 80}, 'Tom Cruise']
[10, 'Audi', 'twenty', 'Changed Value', [40, 50], (60, 70), {'eighty': 80}, 'Tom Cruise']
[10, 'Audi', 'twenty', True, [40, 50], (60, 70), {'eighty': 80}, 'Tom Cruise']
[10]
[20, 'Audi', 'twenty', 'Changed Value', [40, 50], (60, 70), {'eighty': 80}, 'Tom Cruise']
