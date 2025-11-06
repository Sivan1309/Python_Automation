from pwn import *
import sys
from hashlib import sha256
if len(sys.argv) !=2:
        print("Invalid arguments")
        print(f"Usage: python3 {sys.argv[0]} <sha256-hash>") # Example: python3 sha256crack.py d2d2d2...
        exit(1)
        
wanted_hash = sys.argv[1]
password_file = "rockyou.txt"
attempts=0
with log.progress ("SHA256 Cracker") as p:
    with open (password_file, "r") as f: # Open the password list file
        for line in f:
            password = line.strip()
            attempts += 1
            p.status(f"Attempt {attempts}: Trying password '{password}'")
            hashed_password = sha256(password.encode()).hexdigest() # Hash the password
            if hashed_password == wanted_hash:
                p.success(f"[+] Success! Password found: '{password}' after {attempts} attempts") # If successful
                break
        else:
            p.failure("[-] Password not found in the provided list.")
print("SHA256 Cracking completed.")