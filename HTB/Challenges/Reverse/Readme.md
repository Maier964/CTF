
Description:
~~~
Are you able to cheat me and get the flag?
~~~


2 security layers : 
	# One hardcoded string : SuperSeKretKey (found using r2 or ltrace or strings)
	# 20 rand() generated characters using srand(time(0)) as seed.

For the latter, we could set our time as an absolute value, thus giving us the same random chars over and over: 
	(???) Tried to use "faketime" to run the binary with absolutes, didn't work for some reason (?)
	! Opened the binary with r2 in write mode and patched the conditional jmp with a simple jmp -> bypassed the whole time shenanigans. 
