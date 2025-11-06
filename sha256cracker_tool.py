'''
Short summary:
This project implements a high-performance, file-backed SHA-256 dictionary cracker designed for offline recovery and security assessment. Given a target SHA-256 hash and a candidate password list (e.g., rockyou.txt), the tool iterates through each candidate, computes its SHA-256 digest, and reports the first matching plaintext password. The program is instrumented with a progress display, attempt counters, and clear success/failure reporting to make testing and analysis straightforward.

Key features:

Command-line interface that accepts a single SHA-256 hash as input (usage enforced).
Efficient streaming of large wordlists from disk (memory friendly).
Per-attempt progress updates using a console progress logger (pwnlib.log.progress) for real-time feedback.
Accurate SHA-256 computation using Python’s standard hashlib library.
Clean success/failure semantics with attempt counts and graceful termination.

Why this is a capstone-worthy project:
This project ties together practical systems programming, cryptographic primitives, file I/O, and user-facing tooling into a single, usable application. It demonstrates competence in:
building reliable automation scripts for security tasks,
handling large input datasets efficiently,
integrating third-party tooling for a better user experience,
and documenting and testing a security-oriented utility. The project surfaces many real-world concerns (I/O performance, logging, ethical constraints) that are vital for production-level security tooling.

How it works (methodology):
Validate user input (ensure exactly one SHA-256 hash argument).
Open a password candidate file (rockyou.txt) and stream it line by line.

For each candidate:
Strip whitespace, increment the attempt counter.
Compute sha256(candidate.encode()).hexdigest().
Compare to the target hash; on a match, log success and stop.
If the wordlist is exhausted with no match, report failure.
Provide a final completion message.

Intended use-cases (defensive / authorized only):
Recovering forgotten passwords for systems you own and control.
Security assessments on systems and accounts where you have explicit authorization (penetration testing engagements, internal red-team exercises).
Educational demonstrations of why weak passwords and unsalted fast hashes are vulnerable to dictionary attacks.

Ethics & responsible use (mandatory):
This tool is intended for legitimate security testing and recovery only. Unauthorized use to break into accounts, services, or systems is illegal and unethical. Always obtain explicit written permission before performing password recovery or cracking against any account or system that you do not own. When used in an authorized engagement, log activities, protect any recovered secrets, and report findings responsibly.

Limitations & security notes:

SHA-256 is a fast, unsalted hash in this script — while useful for demonstration, it is not suitable for secure password storage. Production systems should use slow, salted algorithms (bcrypt, scrypt, Argon2, PBKDF2).
Effectiveness is limited to the quality and coverage of the provided wordlist; many modern passwords are resistant to dictionary attacks.
This script performs single-threaded checks; for large wordlists a parallelized or GPU-accelerated approach would dramatically increase throughput.

Possible enhancements / future work:
Add multi-threading or process-based parallelism to speed up large cracking jobs.
Integrate GPU acceleration or leverage hashcat for high-performance cracking.
Support salted and iterative hash schemes and the ability to specify salting formats.
Add rate-limited, resumable scanning and checkpoints for very large wordlists.
Produce structured output (JSON) with metadata (found password, attempts, elapsed time) for automated reports.
Add unit tests and CI checks to ensure robustness across environments.

Tech stack / libraries used:

Python 3 standard library (sys, hashlib)
pwntools for console progress logging (pwnlib.log.progress) — improves UX for live runs.
'''
#################################################################################################################################################                                                                         
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

###################################################################################################################################################
'''
Output:
(pwntools-venv) :~/pwntools-venv$ python3 sha256crack.py a075d17f3d453073853f813838c15b8023b8c487038436354fe599c3942e1f95
[+] SHA256 Cracker: [+] Success! Password found: 'p@ssw0rd' after 8 attempts
SHA256 Cracking completed.
'''
