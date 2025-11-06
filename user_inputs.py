def test():

    #------------User Inputs------------#   
    def get_user_inputs():
        user_inputs = {}
        user_inputs['name'] = input("Enter your name: ")
        user_inputs['age'] = int(input("Enter your age: "))
        user_inputs['email'] = input("Enter your email address: ")
        return user_inputs  # Return the dictionary containing user inputs
    if __name__ == "__main__":
        inputs = get_user_inputs()  # Call the function to get user inputs
        print("User Inputs:")  # Print a header for user inputs
        for key, value in inputs.items():  # Iterate through the dictionary items
            print(f"{key}: {value}")  # Print each key-value pair
#     #------------File Handling Examples------------#
# from files import * 
#     # The above line imports all the file handling examples from files.py   
    
    
if (__name__ == "__main__"): # Checking if the script is run directly
            print("Executing as the main module")
            test()
else:
            print("Imported as a module") 
