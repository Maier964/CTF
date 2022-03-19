* Powershell transcript - log file containing history of commands.
* If we cant figure it out, we can check the timestamps and try to order it accordingly.
* Log is mostly filled with useless data ( wrong commands and spelling issues).
* However, we can see that the user (Alice) created a file on Desktop ( whatyouneedishere.txt ) and piped a base64-encoded string in there. Decoding it, we get the flag :
thisisthe1stflag

~~~powershell
"PS C:\Users\alice\Desktop> New-Item "C:\Users\alice\Desktop\whatyouneedishere.txt"


    Directory: C:\Users\alice\Desktop


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         12/8/2020  10:34 AM              0 whatyouneedishere.txt"
~~~

Difficulty : 1/10
