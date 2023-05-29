    mov     ebp, 13AC9741h
    mov     ebx, 0Bh

top:
    movsx   eax, byte ptr [ebx+esi] ; call toUpper on key[ ebx ]
    push    eax             ; Parameter to toupper()
    call    _toupper        ; Call toupper()
    add     esp, 4          ; Fix the stack (__cdecl style)
    cmp     al, 37h         ; if al > 37H ('7' in ascii) -> go to body1 with key[ebx] changed by toUpper()
    mov     byte ptr [ebx+esi], al
    jg      short body1
    mov     ecx, ebp    ; if not, move that constant 13AC9741h to ecx ( this is only on the first iteration btw )
    mov     dl, cl  ; put the first byte of ecx in dl ( is this 41 or 13 ??? ) if little-endian -> 13 ( for the first iteration ) 
    and     dl, 7
    xor     dl, al ; dl = ((first byte of ecx) & 7H) ^ key[ebx] ( changed by toUpper() )
    shr     ecx, 3  ; shift the counter register
    mov     byte ptr [ebx+esi], dl ; put this computed dl into key[ebx]
    mov     ebp, ecx ; global value is now prev >> 3
    jmp     short body2

body1:
    cmp     al, 41h ; if al >= 41H just decrement ebx
    jge     short body2 
    mov     cl, bl ; bl = 0xB in this case
    and     cl, 1 
    xor     cl, al 
    mov     byte ptr [ebx+esi], cl ; key[ebx] = bl  & 1 ^ key[ebx];

body2:
    dec     ebx 
    jns     short top