import binascii
import string

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)

def shortcut_en(char):
    return (123 * char + 18) % 256

test = binascii.unhexlify("6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921")

decoded = ""

for b in test:
    for i in range(0,127):
        if (shortcut_en(i) == b):
            decoded+=chr(i)

print(decoded)



