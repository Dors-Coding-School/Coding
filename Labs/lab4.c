// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

typedef uint8_t BYTE;
typedef int16_t SAMPLE_AUDIO;


int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);
    
    
    BYTE headerBuffer[HEADER_SIZE];
    // TODO: Copy header from input file to output file
    fread(headerBuffer, sizeof(BYTE), HEADER_SIZE, input);
    fwrite(headerBuffer, sizeof(BYTE), HEADER_SIZE, output);

    // TODO: Read samples from input file and write updated data to output file
     // Keep reading data from raw until empty:

    SAMPLE_AUDIO buffer;

    while (fread(&buffer, sizeof(SAMPLE_AUDIO), 1, input) == 1)
    {
        buffer = buffer * factor;
        fwrite(&buffer, sizeof(SAMPLE_AUDIO), 1, output);
    }
    // Close files
    fclose(input);
    fclose(output);
}
