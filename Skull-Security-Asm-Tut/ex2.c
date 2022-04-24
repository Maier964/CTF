#include <stdio.h>
#include <stdlib.h>


// Trying to represent the asm function in c..


void scrabble( char* key )
{
    int cnt = 0xC2;
    int iterator = 0xB;
    while( cnt >= 0x7 )
    {
        iterator--;
        cnt -= 0x11;
        char swapAux;

        key[ cnt % 0xC ] = swapAux;
        swapAux = key[ iterator + 1 ];
        key[ iterator + 1 ] = key[ cnt % 0xC ];
    }
}