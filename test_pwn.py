'''
This code uses pwntools (`pwn`), a lightweight Python toolkit for CTF-style exploit development and binary interaction. 
It provides convenient APIs for spawning processes, connecting remotely, handling ELF/ROP primitives, packing/unpacking, and crafting payloads.
'''
#####################################################################################################################################################


from pwn import *
# Run a local binary
p = process('./vulnerable_binary')

# Send input
p.sendline(b'Hello world')

# Receive output
print(p.recvline())

p.close()

from pwn import *
# Connect to a remote service
p = remote('example.com', 1234) 
# Send input
p.sendline(b'Hello world')
# Receive output
print(p.recvline()) 
p.close()

from pwn import * # Connect to a remote service

try:
    # Replace with actual target host and port
    target_host = '***'
    target_port = 4444
    
    p = remote(target_host, target_port)
    p.sendline(b'Hello world')
    print(p.recvline())
except Exception as e:
    print(f"Connection error: {e}")
finally:
    if 'p' in locals():
        p.close()
        

from pwn import *
# Load an ELF binary and print its symbols
elf = ELF('./vuln')
print(elf.symbols)
print(hex(elf.got['puts'])) # Address of GOT entry for puts
print(hex(elf.plt['puts'])) # Address of PLT entry for puts

from pwn import *
# Generate shellcode for spawning a shell
context.arch = 'amd64'
shellcode = asm(shellcraft.sh())
print(shellcode)

# from pwn import *
# # Exploit a format string vulnerability to overwrite a memory address
# p = process('./fmt_vuln')
# payload = fmtstr_payload(6, {0x601050: 0xdeadbeef})
# p.sendline(payload)
# p.interactive()
