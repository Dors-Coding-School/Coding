#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1
    if (argc != 3)
    {
        printf("Usage: reverse.c input.wav output.wav\n");
        return 1;
    }

    // Open input file for reading
    // TODO #2
    char *infile = argv[1];
    FILE *inptr = fopen(infile, "rb");
    if (inptr == NULL){
        printf("Input is not a WAV file.\n");
        return 1;
    }

    // Read header into an array
    // TODO #3
    WAVHEADER header;
    fread(&header, sizeof(WAVHEADER), 1, inptr);

    // Use check_format to ensure WAV format
    // TODO #4
    if(check_format(header) == 0){
        fclose(inptr);
        printf("Output is not a WAV file.\n");
        return 1;
    }

    // Check if audio format is PCM
    if (header.audioFormat != 1) {
        fclose(inptr);
        printf("Audio format is not PCM.\n");
        return 1;
    }

    // Open output file for writing
    // TODO #5
    char *outfile = argv[2];
    FILE *outptr = fopen(outfile, "wb");
    if (outptr == NULL){
        printf("Could not open %s.\n", outfile);
        return 1;
    }

    // Write header to file
    // TODO #6
    fwrite(&header, sizeof(WAVHEADER), 1, outptr);

    // Use get_block_size to calculate size of block
    // TODO #7
    int size = get_block_size(header);

    // Write reversed audio to file
    // TODO #8
    // If fseek succeed, it'll return 0
    if (fseek(inptr, size, SEEK_END))
    {
        return 1;
    }

    BYTE buffer[size];
    while (ftell(inptr) - size > sizeof(header))
    {
        // Cause fread() move the file pointer size forward
        // So, -2 * size
        if (fseek(inptr, -2 * size, SEEK_CUR))
        {
            return 1;
        }
        fread(buffer, size, 1, inptr);
        fwrite(buffer, size, 1, outptr);
    }

    // TODO #2
    fclose(inptr);

    // TODO #5
    fclose(outptr);
}

int check_format(WAVHEADER header)
{
    // TODO #4
    if(header.format[0] == 'W' && header.format[1] == 'A' && header.format[2] == 'V' && header.format[3] == 'E'){
        return 1;
    }
    return 0;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    // Divide by 8 to convert into bytes
    int size = header.numChannels * header.bitsPerSample / 8;
    return size;
}
