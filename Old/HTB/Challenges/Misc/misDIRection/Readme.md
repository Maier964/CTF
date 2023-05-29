	
Description:
~~~
During an assessment of a unix system the HTB team
found a suspicious directory. They looked at
everything within but couldn't find any 
files with malicious intent.
~~~
    
    ~ Used "find" to list all directories and files in ".secret". Added this output to a file. Used "file" on every line to find that every file was empty, so no hidden files... Then used "tree" to get a better view of the directory and figured out every letter had an index, so it was easy to form a string from that information. Unfortunately, I could not make a script to automate this and I had to manually do it (fuck me!). 
	~ After finding the string, I used an online hash cracker that didn't find anything.. Then I googled the string and found (even tho I didnt want to) that the string is Base64'ed... I decoded it and found the flag..HTB{DIR3ctLy_1n_Pl41n_Si7e}

	!!!!!! Important to remember !!!!!
		$ When CrackStation doesn't provide, try to use CyberChef.
