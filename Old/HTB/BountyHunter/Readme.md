		** Bounty Hunter **




IP : 10.10.11.100

*1. Nmap Enum :*

Starting Nmap 7.91 ( https://nmap.org ) at 2021-09-13 11:18 EDT
Nmap scan report for 10.10.11.100
Host is up (0.11s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
> | ssh-hostkey: ~~~~
|   3072 d4:4c:f5:79:9a:79:a3:b0:f1:66:25:52:c9:53:1f:e1 (RSA)
|   256 a2:1e:67:61:8d:2f:7a:37:a7:ba:3b:51:08:e8:89:a6 (ECDSA)
|_  256 a5:75:16:d9:69:58:50:4a:14:11:7a:42:c1:b6:23:44 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Bounty Hunters
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.87 seconds

*2. Burp Inspection*

 	- The client makes a request with XML data - tried XXE, didn't work (maybe I did something wrong?)
	- Looking at the code, we found that /resoruces/bountylog.js is availabe.
	- Found this intresting function : 
	
	function returnSecret(data) {
	return Promise.resolve($.ajax({
            type: "POST",
            data: {"data":data},
            url: "tracker_diRbPr00f314.php"
            }));

 This .php file ("tracker_diRbPr00f314.php") doesn't tell us anything new.. It seems that the only was to access this is trough some kind of XXE. Got stuck here. We try some dirbuster I guess..
 
 *3. Dirbuster*
 	**We found db.php but we are unable to acces it via client. Dead end for now..
	
	*****FINALLY AFTER 20 TRIES THE BURP XXE FUCKING WORKED BCZ OF FORMATIING ISSUES GOD DAMN!

	
So we found the user to be "development".. We tried infiltrating into /home/development/.ssh/id_rsa but no luck there. So we are left with getting into db.php For this, we use another XXE exploit, targeted towards .php files. 
	
	
Finally, after wasting around 2 hours... : 
	USER : development
	PASS : m19RoAU0hP41A1sTsq6K
	
Let's ssh. ==User flag found..== ( b08cd078cd762a85cde7434da40ed17e )

~~~~~~~Privesc~~~~~~~~~~

Now for the fun part... 
'sudo -l' - found python and a py script 
tried GTFObins for python - no luck 

Finally...After a lot of trail and error, I managed to understand the exploit but it wouldn't work no matter how hard I tried..Then I realised I was using "python3" as an interpreter and that one didnt have sudo permissions on my account.. So of course everything I was executing didn't work... Well.. at least we finally got it.. ROOT : ==444e528d784cd734e975599ebc3d811d==
~~~~~~~~~~~~~~~~~~~~~~~~~


**CONCLUSIONS :  
			ATTENTION IS KEY! I spent half my time working towards mistakes that I've made because I wasn't looking in detail at stuff.. 

			&&& I didn't keep in mind that a specific version of python is granted-sudo (even tho I ran sudo -l)