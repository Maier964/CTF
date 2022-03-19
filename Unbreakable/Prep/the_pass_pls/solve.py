
# bytes found in the global variable of the program
global_var = b"\xb0\x8a\x91\x96\x81\xb6\x97\x86\x88\xb0\xc3\x9d\x94\x81\xc7\x87\x80\xac\x8a\xc3\x86\xac\x95\xc3\x86\x9d\x97\xac\xc2\x87\x8e"

inp = "" 

# input[i] ^ 0xf3 = global_var[i] <-> global_var[i] ^ 0xf3 = input[i]
for c in global_var:
    inp += chr( c ^ 0xf3 )

print(inp)


