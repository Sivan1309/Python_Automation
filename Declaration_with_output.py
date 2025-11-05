def test():
    #----------Variable Declarations and Data Types-----------------------
    print("Hello, World!")
    print("This is a test function.")
    string_example = "This is a sample string."
    number_example = 42 + 84 + 126\
        + 168
    list_example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    dictionary_example = {"key1": "value1", "key2": "value2", "key3": "value3"}
    tuple_example = (True, False, True, False)
    set_example = {3.14, 2.71, 1.61, 0.577}
    print(list_example)
    print(dictionary_example)
    print(tuple_example)
    print(set_example)
    print(string_example)
    print(number_example)
    
if __name__ == "__main__":
    test()

# ---- OUTPUT ----
Hello, World!
This is a test function.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
(True, False, True, False)
{0.577, 1.61, 2.71, 3.14}
This is a sample string.
420
