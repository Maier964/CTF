	Overall an easy challenge
	
	The code seems to handle the RGB light on a discord server somehow. We see that the node js API is linked to a json configuration file which has the host set as local ( 127.0.0.1 ) and some other gibberish... But the token is missing. The token is what we need..
	I proceeded to install nodejs on my machine and then used npm to install all necessary packages to make the .js file run. Unfortunately, that lead nowhere. Then I got stuck.
	(!!!) What I should've done is check for hidden folders with "ls -a" and ofc find the ".git" commit. Then, we see that logs are available and we just fetch the log in which the guy didnt hide the login token. Basic stuff, I just need to be more attentive and not give up so early, this should have been solved waay faster..
