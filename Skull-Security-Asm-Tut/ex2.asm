   
 ; This example is the first step in Starcraft's CDKey Decode. This shuffles the characters in the key in a predictable way. 
   
   
   lea     edi, [esi+0Bh] ; 12 characters between esi and edi; edi - pointer to the last character
   mov     ecx, 0C2h ; 0xC2 in ecx - for loops
top:
   mov     eax, ecx ; put ecx in eax
   mov     ebx, 0Ch ; put 12 in ebx - length of the key
   cdq ; covert eax to edx:eax 64 bit ( for signed division ) 
   idiv    ebx ; eax = eax / ebx    and       ; edx = eax % ebx
   mov     al, [edi] ; put last character of key in the lower byte of ax  => idiv was modular ( eax is overwritten )
   sub     ecx, 11h ; ecx = ecx - 11h
   dec     edi  ; decrement iterator - going from last char to first
   cmp     ecx, 7 ; if ecx > 7 jump to top
   mov     bl, [edx+esi] ; put key[ eax modulus ] in bl
   mov     [edi+1], bl ; key[ iterator + 1 ]  = key[ eax modulus ]
   mov     [edx+esi], al ; key [ eax modulus ] = key[ iterator ]
   jge     top