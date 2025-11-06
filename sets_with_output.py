# A set is an unordered collection of unique elements in Python.
# It automatically removes duplicates and is useful for membership tests,
# mathematical operations like union, intersection, and handling distinct values.


def test():
    #-------------sets-------------
    set_example = {1, 2, 3, 4, 5, 5, 4, 3,  2, 1}  # Duplicates will be removed
    print(set_example)
    set_example.add(6)  # Adding an element
    print(set_example)
    set_example.remove(3)  # Removing an element
    print(set_example)
    set_example.discard(10)  # Removing an element that may not exist (no error)
    print(set_example)
    print(len(set_example))  # Length of the set
    print(2 in set_example)  # Membership test
    another_set = set((4, 5, 6, 7, 8)) # Creating another set using set() constructor
    print(set_example.union(another_set))  # Union of two sets
    print(set_example.intersection(another_set))  # Intersection of two sets
    print(set_example.difference(another_set))  # Difference of two sets  
    another_set.update({9,10})  # Updating set with new elements
    print(another_set)  
    super_set = set_example.copy()  # Copying a set
    print(super_set)
    super_set.update(another_set)  # Updating copied set with another set
    print(super_set)    
    list_from_set = list(super_set)  # Converting set to list
    print(list_from_set)
    super_set.update([11,12,13])  # Updating set with elements from a list  
    print(super_set)
    super_set.update(list_from_set)  # Updating set with elements from a list  
    print(super_set)
    super_set.discard(2)  # Discarding an element
    print(super_set)
    print(list_from_set)
    super_set.pop()  # Removing and returning an arbitrary element
    print(super_set)
    print(super_set)
    print(super_set)
    
if (__name__ == "__main__"): # Checking if the script is run directly
        print("Executing as the main module")
        test()
else:
        print("Imported as a module") 

# ---- OUTPUT ----
Imported as a module
{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5, 6}
{1, 2, 4, 5, 6}
{1, 2, 4, 5, 6}
5
True
{1, 2, 4, 5, 6, 7, 8}
{4, 5, 6}
{1, 2}
{4, 5, 6, 7, 8, 9, 10}
{1, 2, 4, 5, 6}
{1, 2, 4, 5, 6, 7, 8, 9, 10}
[1, 2, 4, 5, 6, 7, 8, 9, 10]
{1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
{1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
{1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
[1, 2, 4, 5, 6, 7, 8, 9, 10]
{4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
{4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
{4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
