#include <stdio.h>
#include <stdlib.h>

// Trying to represent the asm function in C 

int func( char* key ) {
    int val = 3;
    for( int i = 0; i < 0xC; i++ ) {
        val += (key[i] - '0') ^ (val*2);
    }

    if ( key[ 0xC ] == ((val % 10) + '0') )
        return 1;
    else 
        return 0;
}