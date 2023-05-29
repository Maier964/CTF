#!/usr/bin/python3
from ntpath import join
import os
from pwn import *

#flag = open('flag.txt', 'r').read().strip().encode()

# encode() with no params just converts the input to byte form

class XOR:
    def __init__(self):
        self.key = os.urandom(4)
    def encrypt(self, data: bytes) -> bytes:
        xored = b''
        for i in range(len(data)):
            xored += bytes([data[i] ^ self.key[i % len(self.key)]])
        return xored
    def decrypt(self, data: bytes) -> bytes:
        return self.encrypt(data)

    # Solve problem in a method of the encryption class ;)

    def solve(self) -> None:
        output = unhex("134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9") #output was presented in a txt file
        #key is 4 bytes, first 4 characters of the flag is most likely "HTB{" -> find key by xoring the first 4 bytes of output with "HTB{"
        key = []
        flag = b'HTB{'

        for i in range(0,4):
            key.append(output[i] ^ flag[i])

        print(bytes(key)) #found key!

        flag = []

        for i in range(len(output)):
            flag.append(output[i] ^ key[ i % len(key) ])


        print( bytes(flag).decode() )

        

def main():
    global flag
    crypto = XOR()
#    print ('Flag:', crypto.encrypt(flag).hex())
    crypto.solve()

if __name__ == '__main__':
    main()
