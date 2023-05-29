IP : 10.10.10.245

Open ports : 
 
	21 (FTP) : 
	~ User anonymous is okay, but password isn't.. Weird. 
	22 (SSH) 
	80 (HTTP) :
	~ Using gunicorn (Googled and seems to be vulnerable to HTTP Response Spitting, check burp)
	~ Seems to have a packet capture for each session... Fortunately, the session displayed is right on the URL, so we just fetch the data from the first session with a convenient "download" button that the dev implemented on the dashboard
	~ Analysing the packet, we get the FTP creds (nathan:Buck3tH4TF0RM3!)
	~ The FTP server is actually the home directory of nathan lul.. 
	~ Tried SSH and ofc it worked and got the user own.. Now let's try some privesc
		: Ran linpeas, found that some python thingy was marked as 95% privesc... Went to GTFO bins and after 2 tries, succeded in getting root.. Kinda script kiddie-ish tho, I need to understand all this to be sure I'm good enough.
