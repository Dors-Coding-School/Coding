#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // Your program must first ask the user for a message using get_string
    string message = get_string("Message: ");


    // Iterate through each character in the message
    for (int i = 0, n = strlen(message); i < n; i++)
    {
        // Convert the character to an 8-bit binary number
        unsigned char byte = message[i];
        for (int j = BITS_IN_BYTE - 1; j >= 0; j--)
        {
            // Get the jth bit of the byte
            int bit = (byte >> j) & 1;

            // Print the bit using the provided print_bulb function
            print_bulb(bit);
        }
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
