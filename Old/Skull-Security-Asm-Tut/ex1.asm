; Note: ecx is a pointer to a 13-digit Starcraft cdkey
; This is a function that returns 1 if it's a valid key, or 0 if it's invalid

   mov     eax, 3 
   mov     esi, ecx ; put the start address of the key in a static non-volatile register
   xor     ecx, ecx ; clean ecx to use it for counting
 Top:
   movsx   edx, byte ptr [ecx+esi] ; put each byte from esi in edx
   sub     edx, 30h ; subtract 0x30  ow damn to make it an int! it is a string currently!
   lea     edi, [eax+eax]  ; edi = eax * 2
   xor     edx, edi ; idk
   add     eax, edx ; eax = eax + prev value 
   inc     ecx ; increment the iterator
   cmp     ecx, 0Ch ; go until 0C with the iterator
   jl      short Top

    ; for finished
   xor     edx, edx ; clear edx
   mov     ecx, 0Ah ; put 10(dec) in ecx
   div     ecx  ; eax = edx:eax / ecx <=> eax = eax / 10 AND edx = eax % 10

   movsx   eax, byte ptr [esi+0Ch]  ; get the last byte of the key in eax
   add     edx, 30h ;
   cmp     eax, edx ; compare last byte with 30h, if not equal, jump to bottom returning 0 (eax xor eax)
   ; if true, return 1 ( eax = 1 )
   jnz     bottom

   mov     eax, 1
   ret

 bottom:
   xor     eax, eax ; 
   ret