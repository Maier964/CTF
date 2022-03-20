# Paper #

IP : 10.10.11.143

1. Nmap Scan


~~~bash
# Nmap 7.91 scan initiated Mon Feb 21 15:16:53 2022 as: nmap -sV -oA paper 10.10.11.143
Nmap scan report for 10.10.11.143
Host is up (0.096s latency).
Not shown: 996 closed ports
PORT     STATE    SERVICE  VERSION
22/tcp   open     ssh      OpenSSH 8.0 (protocol 2.0)
80/tcp   open     http     Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1k mod_fcgid/2.3.9)
443/tcp  open     ssl/http Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1k mod_fcgid/2.3.9)
1500/tcp filtered vlsi-lm

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Feb 21 15:17:20 2022 -- 1 IP address (1 host up) scanned in 26.61 seconds
~~~

2. Enumeration

* Http page / Https page doesn't show anything useful, it is the default Apache page. The only information that was gathered was that the Apache version is 2.4, because the port had an /manual directory..

* Gobuster didn't catch anything else...

* Tried some common Apache 2.4 CVEs, nothing worked.. Felt stuck so decided to take a look at the forums. A suggestion was to use nikto. With that, I found a subdomain called office. Now things got real.

* Office subdomain contained a (guess what) WordPress blog. WPScan gave us some valuable info 
![not found](Pasted%20image%2020220221164424.png "1")

3. Foothold

* This particular post stood out:
![not found](Pasted%20image%2020220221164807.png "2")

* After more enumeration, stumbled upon this link: https://www.exploit-db.com/exploits/47690

* Found link for chat: http://chat.office.paper/register/8qozr226AhkCHZdyY 

* Registered and played with the bot.. Got this :

export ROCKETCHAT_USER=recyclops  
export ROCKETCHAT_PASSWORD=Queenofblad3s!23

![not found](Pasted%20image%2020220221173556.png "3")

Finish explaining privesc(todo)

