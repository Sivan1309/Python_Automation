
# A dictionary is an unordered, mutable collection of key–value pairs in Python.
# Each key must be unique, and it provides fast lookups, updates, and deletions.
# Dictionaries are commonly used to store structured data and map one value to another.


def test():

#-------------Dictionaries-------------

    dictionary_example = {"apple": 1, "banana": 2, "cherry": 3}
    print(dictionary_example)
    dictionary_example["date"] = 4  # Adding a new key-value pair
    print(dictionary_example)
    dictionary_example.pop("banana")  # Removing a key-value pair
    print(dictionary_example)
    dictionary_example["cherry"] = 33  # Modifying a value
    print(dictionary_example)
    print(dictionary_example["apple"])  # Accessing a value by key
    print(len(dictionary_example))  # Length of the dictionary
    print("banana" in dictionary_example)  # Membership test for key
    print(dictionary_example.get("cherry"))  # Accessing a value using get method
    print(dictionary_example.keys())  # Getting all keys
    print(dictionary_example.values())  # Getting all values
    print(dictionary_example.items())  # Getting all key-value pairs
    for key, value in dictionary_example.items():  # Iterating over key-value pairs
        print(f"{key}: {value}")  
if (__name__ == "__main__"): # Checking if the script is run directly
        print("Executing as the main module")
        test()
else:
        print("Imported as a module") 

# ---- OUTPUT ----
Imported as a module
{'apple': 1, 'banana': 2, 'cherry': 3}
{'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4}
{'apple': 1, 'cherry': 3, 'date': 4}
{'apple': 1, 'cherry': 33, 'date': 4}
1
3
False
33
dict_keys(['apple', 'cherry', 'date'])
dict_values([1, 33, 4])
dict_items([('apple', 1), ('cherry', 33), ('date', 4)])
apple: 1
cherry: 33
date: 4
