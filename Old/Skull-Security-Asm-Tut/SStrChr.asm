; Imported from char *__stdcall SStrChr(const char *str, int c); (Storm.dll)


                 push    ebp ; save ebp because it is non-volatile
                 mov     ebp, esp ; initialize stack frame
                 mov     eax, [ebp+arg_0] ; put first argument of function in eax
                 test    eax, eax ; test if this arg is 0, if so
                 jnz     short loc_1

                 push    57h             ; push an error code on the stack ( ERR_INVALID_PARAMETER ) 
                 call    ds:SetLastError ; call the function which will set the error message
                 xor     eax, eax ; clean eax register ( return 0 ) 
                 pop     ebp ; restore ebp
                 retn    8 ; return 8 to clean up the stack variables -> we got 8 bytes on the stack -> 2 variables?
                 ; a pointer and an int maybe, we'll see ( provided that we dont have the function signature at line 1, we try to guess)
 ; ---------------------------------------------------------------------------

 loc_1: ; valid first param
                 mov     cl, [eax] ; eax being dereferenced -> eax is a pointer -> 
                 ; first param is a pointer -> string potentially? 
                 test    cl, cl ; test is dereferenced value is != 0; if it is, perform clean up and leave ( loc_3 jmp )
                 jz      short loc_3 
                 mov     dl, [ebp+arg_4] ; put the other param in dl -> put only the first byte of that param -> param is a char (possible)
                 jmp     short loc_2
 ; ---------------------------------------------------------------------------

 loc_2:
                 cmp     cl, dl ; compare the two prev values
                 jz      short loc_4 ; if they are the same, leave and return the remaining eax substring (note we dont do any xor eax eax when returning)
                 mov     cl, [eax+1] ; advance to the next character of the string
                 inc     eax ; increment the pointer to point to the next character
                 test    cl, cl ; if cl != 0, continue the loop and compare
                 jnz     short loc_2

 loc_3:
                 xor     eax, eax ; return 0

 loc_4:
                 pop     ebp
                 retn    8

; why is the second param passed as an int if we only need the first byte? strange implementation
; I will not convert this code to C since it is pretty clear what it does. It is a basic strchr, enchanted with null character checking.