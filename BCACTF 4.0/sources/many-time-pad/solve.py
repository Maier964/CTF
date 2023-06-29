from Crypto.Util.number import long_to_bytes, bytes_to_long


def rev_enc(plain, key):
    return long_to_bytes( bytes_to_long(plain) ^ bytes_to_long(key) )


""" 
* C_FLAG = P_FLAG xor Key
* C_Grocery = P_Grocery xor Key 

    This is a known plaintext attack. 
    1. We know the plaintext grocery list,
    2. We also know the ciphertext of the grocery list -> Key is found (because of the xor proprieties).
    3. Once key in found, we have P_FLAG, just find C_FLAG

"""

C_FLAG = open("many-time-pad.out", "rb").read()
C_Grocery = open("grocery-list.out", "rb").read()
P_Grocery = b"I need to buy 15 eggs, 1.7 kiloliters of milk, 11000 candles, 12 cans of asbestos-free cereal, and 0.7 watermelons."


key = rev_enc( C_Grocery, P_Grocery )

print( rev_enc(C_FLAG, key) )
