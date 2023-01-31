#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;
const int BASE = 2;

void print_bulb(int bit);

int main(void)
{
    string message = get_string("Message: ");
    for (int i = 0, n = strlen(message); i < n; i++)
    {
        unsigned char byte = message[i];
        int binary[BITS_IN_BYTE];
        int quotient = byte;
        int remainder;

        // convert character to binary
        for (int j = 0; j < BITS_IN_BYTE; j++)
        {
            remainder = quotient % BASE;
            binary[j] = remainder;
            quotient /= BASE;
        }

        // print binary representation
        for (int j = BITS_IN_BYTE - 1; j >= 0; j--)
        {
            print_bulb(binary[j]);
        }
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        printf("\U0001F7E1");
    }
}
