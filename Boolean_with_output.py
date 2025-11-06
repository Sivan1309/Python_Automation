def test():
#-----------Booleans and Operators-------------
    valid = True
    invalid = False
    print(type(valid))
    print(type(invalid))
    print("Valid AND Invalid:", valid and invalid) # Logical AND
    print("Valid OR Invalid:", valid or invalid)   # Logical OR
    print("NOT Valid:", not valid)                  # Logical NOT
    print("Valid XOR Invalid:", valid ^ invalid)   # Logical XOR
    print("Valid is equal to Invalid:", valid == invalid) # Equality check
    print("Valid is not equal to Invalid:", valid != invalid) # Inequality check
    print(not valid) # Negation
    print(not invalid) # Negation
    print("*************************\n")
    print((10<90)== True) # Comparison and equality check
    print((10>90)!= False) # Comparison and inequality check 
    print((5<=5) and (3>=2)) # Combined comparisons with logical AND
    print((5<3) or (2>1)) # Combined comparisons with logical OR 
    print((7==7) ^ (4!=4)) # Combined comparisons with logical XOR
    print(2!=1)
    print("*************************\n")
    print(10/6)  # Division
    print(10//6)  # Floor Division
    print(10%6)  # Modulus
    print(10**10)  # Exponentiation
    print("*************************\n")
    
    x=10
    x+=1  # Augmented Assignment
    print(x)
    x-=2  # Augmented Assignment
    print(x)
    x*=3  # Augmented Assignment
    print(x)
    x/=4  # Augmented Assignment
    print(x)
    x//=5  # Augmented Assignment
    print(x)
    x%=6  # Augmented Assignment
    print(x)
    x**=2  # Augmented Assignment
    print(x)
    x=13
    print(bin(x))  # Binary representation
    print(bin(x)[2:].rjust(4,"0"))  # Binary without '0b' prefix and padded witho zeros
    y=5
    print(bin(y))  # Binary representation
    print(bin(y)[2:].rjust(4,"0"))  # Binary without '0b' prefix and padded with zeros
    print("*************************\n")
    print(bin(x & y)[2:].rjust(4,"0"))  # Bitwise AND
    print(bin(x | y)[2:].rjust(4,"0"))  # Bitwise OR    
    print(bin(x ^ y)[2:].rjust(4,"0")) # Bitwise XOR
    print(bin(~x & 0b1111)[2:].rjust(4,"0"))  # Bitwise NOT (4 bits)
    print(bin(x << 2)[2:].rjust(6,"0"))  # Left Shift
    print(bin(x >> 2)[2:].rjust(4,"0"))  # Right Shift
    
if (__name__ == "__main__"): # Checking if the script is run directly
        print("Executing as the main module")
        test()
else:
        print("Imported as a module") 

# ---- OUTPUT ----
Imported as a module
<class 'bool'>
<class 'bool'>
Valid AND Invalid: False
Valid OR Invalid: True
NOT Valid: False
Valid XOR Invalid: True
Valid is equal to Invalid: False
Valid is not equal to Invalid: True
False
True
*************************

True
False
True
True
True
True
*************************

1.6666666666666667
1
4
10000000000
*************************

11
9
27
6.75
1.0
1.0
1.0
0b1101
1101
0b101
0101
*************************

0101
1101
1000
0010
110100
0011
