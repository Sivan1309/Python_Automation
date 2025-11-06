def test():

 #---------------Conditional Statements-------------  

    if True:
        print("True")
    else:
        print("False")
 
try:
    num = int(input("Enter an integer: "))
    print(f"You entered the integer {num}")
except ValueError:
    print("That was not a valid integer.")
    exit(1) 
if (num > 5):
        print(f"{num} is greater than 5")
elif (num == 5):
        print(f"{num} is equal to 5")
else:
        print(f"{num} is less than 5") 
        
print("Amazing") if num % 2 == 0 else print("Incredible") # Ternary conditional operator     
       
 
 #------------Loops------------- 
counter = 0
# while loop
while counter < 20:  
        counter += 1
        print("Counter value:", counter)
        if counter == 15:
            print("Counter reached 15, breaking the loop.")
            break  # Exit the loop when counter reaches 15
        if counter % 2 == 0:
            print("Counter is even, continuing to next iteration.")
            continue  # Skip the rest of the loop for even counter values     
        
#for loop
for i in range(1, 10):  # Looping from 1 to 10
        print("Current number:", i+6)
        if i == 17:
            print("Number is 7, breaking the loop.")
            break  # Exit the loop when i is 7
        if i % 2 != 0:
            print("Number is odd, continuing to next iteration.")
            continue  # Skip the rest of the loop for odd numbers   
for char in "Aslandegrandebureaucarateswidingster":  # Looping through each character in the string
        print("Current character:", char)
        if char == "o":
            print("Character is 'o', breaking the loop.")
            break  # Exit the loop when character is 'o'
        if char in "aeiou":
            print("Character is a vowel, continuing to next iteration.")
            continue  # Skip the rest of the loop for vowels      
for item in [100, "hello", 3.14, True, [1, 2, 3]]:  # Looping through each item in the list
        print("Current item:", item)
        if item == 3.14:
            print("Item is 3.14, breaking the loop.")
            break  # Exit the loop when item is 3.14
        if isinstance(item, str):
            print("Item is a string, continuing to next iteration.")
            continue  # Skip the rest of the loop for string items
for i in range(1, 6):  # Nested loops
        for j in range(1, 4):
            print(f"i: {i}, j: {j}")
            if j == 2:
                print("j is 2, breaking inner loop.")
                break  # Exit the inner loop when j is 2
        print("Completed inner loop for i =", i)
        
 #---------pass statement-------------       
        
for number in range(1, 11):  # Looping through numbers 1 to 10
        if number % 2 == 0:
            pass  # Placeholder for even numbers
        else:
            print("Odd number:", number)
            
            
if (__name__ == "__main__"): # Checking if the script is run directly
        print("Executing as the main module")
        test()
else:
        print("Imported as a module") 

# ---- OUTPUT ----
Enter an integer: You entered the integer 25
25 is greater than 5
Incredible
Counter value: 1
Counter value: 2
Counter is even, continuing to next iteration.
Counter value: 3
Counter value: 4
Counter is even, continuing to next iteration.
Counter value: 5
Counter value: 6
Counter is even, continuing to next iteration.
Counter value: 7
Counter value: 8
Counter is even, continuing to next iteration.
Counter value: 9
Counter value: 10
Counter is even, continuing to next iteration.
Counter value: 11
Counter value: 12
Counter is even, continuing to next iteration.
Counter value: 13
Counter value: 14
Counter is even, continuing to next iteration.
Counter value: 15
Counter reached 15, breaking the loop.
Current number: 7
Number is odd, continuing to next iteration.
Current number: 8
Current number: 9
Number is odd, continuing to next iteration.
Current number: 10
Current number: 11
Number is odd, continuing to next iteration.
Current number: 12
Current number: 13
Number is odd, continuing to next iteration.
Current number: 14
Current number: 15
Number is odd, continuing to next iteration.
Current character: A
Current character: s
Current character: l
Current character: a
Character is a vowel, continuing to next iteration.
Current character: n
Current character: d
Current character: e
Character is a vowel, continuing to next iteration.
Current character: g
Current character: r
Current character: a
Character is a vowel, continuing to next iteration.
Current character: n
Current character: d
Current character: e
Character is a vowel, continuing to next iteration.
Current character: b
Current character: u
Character is a vowel, continuing to next iteration.
Current character: r
Current character: e
Character is a vowel, continuing to next iteration.
Current character: a
Character is a vowel, continuing to next iteration.
Current character: u
Character is a vowel, continuing to next iteration.
Current character: c
Current character: a
Character is a vowel, continuing to next iteration.
Current character: r
Current character: a
Character is a vowel, continuing to next iteration.
Current character: t
Current character: e
Character is a vowel, continuing to next iteration.
Current character: s
Current character: w
Current character: i
Character is a vowel, continuing to next iteration.
Current character: d
Current character: i
Character is a vowel, continuing to next iteration.
Current character: n
Current character: g
Current character: s
Current character: t
Current character: e
Character is a vowel, continuing to next iteration.
Current character: r
Current item: 100
Current item: hello
Item is a string, continuing to next iteration.
Current item: 3.14
Item is 3.14, breaking the loop.
i: 1, j: 1
i: 1, j: 2
j is 2, breaking inner loop.
Completed inner loop for i = 1
i: 2, j: 1
i: 2, j: 2
j is 2, breaking inner loop.
Completed inner loop for i = 2
i: 3, j: 1
i: 3, j: 2
j is 2, breaking inner loop.
Completed inner loop for i = 3
i: 4, j: 1
i: 4, j: 2
j is 2, breaking inner loop.
Completed inner loop for i = 4
i: 5, j: 1
i: 5, j: 2
j is 2, breaking inner loop.
Completed inner loop for i = 5
Odd number: 1
Odd number: 3
Odd number: 5
Odd number: 7
Odd number: 9
Imported as a module
True
