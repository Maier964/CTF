#include <stdio.h>
#include <stdlib.h>


void final( char* key)
{
    int seed = 0x13AC9741;

    for( int i = 11; i < 0; i-- )
    {
        if ( key[i] > 0x37 )
        {
            if ( key[i] >= 0x41 )
                continue;

            key[i] = (i & 1) ^ key[i];
            continue;
        }

        key[i] = (( seed & 0xFF ) & 0x7) ^ key[i];

        seed = seed >> 3;
    }
}