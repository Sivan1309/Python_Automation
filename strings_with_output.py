def test():   
    string_example_1 = "catie"
    string_example_2 = "dog"
    string_length = len(string_example_1) + \
        len(string_example_2)
    print("Length of both the strings:",string_length)
    string_length = "len(string_example_1) + len(string_example_2)"
    print(type(string_example_1))
    print(type(string_length))
    
     # -----------String Formatting-------------
    string_1 = "I am an amazing string"
    string_2 = 'I am another amazing string'
    string_3 = """I am another
    amazing string that spans
    multiple lines"""
    string_4 = '''I am yet another
    amazing string that spans
    multiple lines'''
    string_5 = "He said, \"Hello!\""
    string_6 = 'It\'s a beautiful day!'
    string_7 = "This is a backslash: \\ with more text.\nNew line starts here."
    string_8 = "This is a raw string: C:\\new_folder\\test.\x74\x78\x74" #I have used hex values for 't', 'x', 't'
    string_9 = r"This is a raw string: C:\new_folder\test.txt" #Using 'r' to denote raw string
    string_10 = f"This is a formatted string with a variable: {string_1}" #Using 'f' for formatted string
    string_10 += f" and another variable: {len(string_1)}" #Appending more formatted content
   
    
    string_11_=" This is a messy string      $$$$$$$$$$***    !!!!!!    "    
    print(string_1)
    print(string_2)
    print(string_3)
    print(string_4)
    print(string_5)
    print(string_6)
    print(string_7)
    print(string_8)
    print(string_9)
    print(string_10)
    print("Hello0" in string_5) # Checking substring presence
    print(string_5)
    print(string_5.startswith("He said")) # Checking start of string
    print(string_6)
    print(string_6.endswith("day!")) # Checking end of string
    print(string_1)
    print(string_1[10:17]) # Slicing string from index 10 to 16
    print(string_1.upper()) # Converting to uppercase
    print(string_1.lower()) # Converting to lowercase
    print(string_1.replace("amazing", "incredible")) # Replacing substring
    print(string_1.split(" ")) # Splitting string into list of words
    print(string_1.index("amazing")) # Finding index of substring
    print(string_11_.strip(" $*!")) # Stripping unwanted characters from both ends
    print(string_11_.lstrip(" $*!")) # Stripping unwanted characters from left end
    print(string_11_.rstrip(" $*!")) # Stripping unwanted characters from right end
    print(string_11_.replace(" ", "").replace("$", "").replace("*", "").replace("!", "")) # Removing all unwanted characters
    print(string_11_.split()) # Splitting by whitespace 
    print(string_11_.encode("utf-8")) # Encoding string to bytes    
    print(string_1.rjust(50, "*")) # Right justifying string
    print(string_1.ljust(50, "X")) # Left justifying string
    print(string_1.center(50, "G")) # Centering string

if (__name__ == "__main__"): # Checking if the script is run directly
        print("Executing as the main module")
        test()
else:
        print("Imported as a module") 


# ---- OUTPUT ----
Imported as a module
Length of both the strings: 8
<class 'str'>
<class 'str'>
I am an amazing string
I am another amazing string
I am another
    amazing string that spans
    multiple lines
I am yet another
    amazing string that spans
    multiple lines
He said, "Hello!"
It's a beautiful day!
This is a backslash: \ with more text.
New line starts here.
This is a raw string: C:\new_folder\test.txt
This is a raw string: C:\new_folder\test.txt
This is a formatted string with a variable: I am an amazing string and another variable: 22
False
He said, "Hello!"
True
It's a beautiful day!
True
I am an amazing string
azing s
I AM AN AMAZING STRING
i am an amazing string
I am an incredible string
['I', 'am', 'an', 'amazing', 'string']
8
This is a messy string
This is a messy string      $$$$$$$$$$***    !!!!!!    
 This is a messy string
Thisisamessystring
['This', 'is', 'a', 'messy', 'string', '$$$$$$$$$$***', '!!!!!!']
b' This is a messy string      $$$$$$$$$$***    !!!!!!    '
****************************I am an amazing string
I am an amazing stringXXXXXXXXXXXXXXXXXXXXXXXXXXXX
GGGGGGGGGGGGGGI am an amazing stringGGGGGGGGGGGGGG
