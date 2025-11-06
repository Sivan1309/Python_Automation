# This section demonstrates various file-handling operations in Python, including
# opening files in different modes such as read ('r'), read text ('rt'), read
# binary ('rb'), write ('w'), and append ('a'). It illustrates how to read an
# entire file, read line-by-line, use seek() to reposition the file pointer, and
# iterate through file contents. The code also shows how write and append modes
# create or modify files, how attempting to write to a closed file raises an error,
# and how to retrieve useful file attributes like name, mode, and closed status.
# Additionally, it highlights the importance of using the 'with' statement for
# safe and automatic file resource management, ensuring files are properly closed.
# Finally, it includes a practical example of reading only the top five lines of
# a file using slicing after reading all lines into memory.

def test():

    f = open('simple.txt', 'r') # Open the file in read mode
    print(f.read()) # Read and print the entire content of the file
    f.close() 
    print('------------------------------------------------------')   
    f = open('simple.txt', 'rt')# Open the file in read text mode
    print(f) # Print the file object
    print(f.readlines()) # Read and print the entire content of the file as a list of lines
    print(f.readline()) # Read and print the first line of the file
    f.seek(0) # Move the cursor back to the beginning of the file
    print(f.readline()) # Read and print the first line of the file
    f.seek(0) # Move the cursor back to the beginning of the file
    for line in f: # Iterate through each line in the file
        print(line.strip()) # Print each line after stripping whitespace # Print a separator line
    print('------------------------------------------------------')   
    f = open('simple.txt', 'rb') # Open the file in read binary mode
    print(f.read()) # Read and print the entire content of the file in binary mode  
    f.close()

    f=open("test.txt","w") # Open the file in write mode
    f.write("Hello World\n") # Write "Hello World" followed by a newline to the file
    f.write("Welcome to File Handling in Python\n") # Write another line to the file
    f.close() # Close the file
    # f.write("This will raise an error") # Attempt to write to the closed file, which will raise an error
    print('------------------------------------------------------')   
    f = open('test.txt', 'a') # Open the file in append mode
    f.write("This line is appended.\n") # Append a new line to the file
    f.close() # Close the file
    f = open('test.txt', 'r') # Open the file in read mode
    print(f.read()) # Read and print the entire content of the file
    f.close()
    print('------------------------------------------------------')
    print(f.name) # Print the name of the file
    print(f.mode) # Print the mode in which the file was opened
    print(f.closed) # Print whether the file is closed or not

    with open('rockyou.txt', 'w') as f: # Open the file in write mode using a context manager
        f.write("This file is created using 'with' statement.\n") # Write a line to the file
        f.write("It ensures proper resource management.\n") # Write another line to the file
        print("Inside 'with' block:") # Print a message indicating we are inside the 'with' block
        print(f.closed) # Print whether the file is closed or not (should be False) # Close the file
    print("Outside 'with' block:") # Print a message indicating we are outside the 'with' block
    print(f.closed) # Print whether the file is closed or not (should be True)

    with open('passphrase.txt', encoding='latin-1') as f: # Open the file in default read mode using a context manager
        lines = f.readlines()
        top_5 = lines[:5]
        for line in top_5:
            print(line.strip())
            
if (__name__ == "__main__"): # Checking if the script is run directly
            print("Executing as the main module")
            test()
else:
            print("Imported as a module") 


# ---- OUTPUT ----
Imported as a module
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

This sample TXT file is provided by Sample-Files.com. Visit us for more sample files and resources.
------------------------------------------------------
<_io.TextIOWrapper name='simple.txt' mode='rt' encoding='UTF-8'>
['Lorem ipsum dolor sit amet, consectetur adipiscing elit. \n', 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n', '\n', 'This sample TXT file is provided by Sample-Files.com. Visit us for more sample files and resources.']

Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

This sample TXT file is provided by Sample-Files.com. Visit us for more sample files and resources.
------------------------------------------------------
b'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nSed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\nThis sample TXT file is provided by Sample-Files.com. Visit us for more sample files and resources.'
------------------------------------------------------
Hello World
Welcome to File Handling in Python
This line is appended.

------------------------------------------------------
test.txt
r
True
Inside 'with' block:
False
Outside 'with' block:
True
123456
12345
123456789
password
iloveyou
