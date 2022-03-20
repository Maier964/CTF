## Canvas

Description:
~~~
We want to update our website but we are unable to because the developer who coded this left today. Can you take a look?
~~~

* We are given a local website which has a login form, some unimportant css and obfuscated js. 
* Using the "admin"-"admin" combination on the login form (or just accesing the "dashboard.html" from the URI) provides us with a page where the flag is obfuscated (with a facepalm emoji). We are left with the task of deobfuscating the .js file. 
* The browser colour formatted hints that the last instruction of the file is the one we are looking for (pure intuition here, it was a guessing game after all, I wouldn't deobfuscate all the input, it would take too much... Actually I should write a script to do this!! - note for later). We use a convenient hex_to_string decoder to get the flag : HTB{W3Lc0m3_70_J4V45CR1p7_d30bFu5C4710N}. 
