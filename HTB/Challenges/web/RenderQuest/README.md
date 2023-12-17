# Render Quest

**CHALLENGE DESCRIPTION**

You've found a website that lets you input remote templates for rendering. Your task is to exploit this system's vulnerabilities to access and retrieve a hidden flag. Good luck!

Simple web page where the only user input is related to a template link:

![Untitled](Render%20Quest%20f08e193a0f8b403499d4f0abd541489b/Untitled.png)

Inspecting the source code, we get important information:

- The app is written in go, thus, it uses Go’s templating engine
- The app allows remote and local files to act as templates.
- The object that is passed in the template engine has a method with ‘exec’-like functionality:

![Untitled](Render%20Quest%20f08e193a0f8b403499d4f0abd541489b/Untitled%201.png)

Conclusion: Evident STTI 😊

Since we cannot add local files, let’s start a python http server and forward it to the clearnet with ngrok.

 

![Untitled](Render%20Quest%20f08e193a0f8b403499d4f0abd541489b/Untitled%202.png)

![Untitled](Render%20Quest%20f08e193a0f8b403499d4f0abd541489b/Untitled%203.png)

Now we need the template file. For this, using the hacktricks reference is more than enough:

[https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#ssti-in-go](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#ssti-in-go)

At first, we should confirm the STTI by using the simple {{ . }} payload.

The result:

![Untitled](Render%20Quest%20f08e193a0f8b403499d4f0abd541489b/Untitled%204.png)

Accessing the desired method to gain RCE, payload becomes {{ .FetchServerInfo "whoami" }}

 

![Untitled](Render%20Quest%20f08e193a0f8b403499d4f0abd541489b/Untitled%205.png)

A reverse shell is possible at this point, but using another ngrok instance is tiresome so I’ll just see where the flag is and read it, with the {{ .FetchServerInfo "ls /" }} payload:

![Untitled](Render%20Quest%20f08e193a0f8b403499d4f0abd541489b/Untitled%206.png)

The final payload: 

{{ .FetchServerInfo "cat /flag7b57d586de.txt" }}