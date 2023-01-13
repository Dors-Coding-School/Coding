#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input) {
    int length = strlen(input);
    if (length == 1) {
        // Base case: if the input string is of length 1, return the integer value of the last character
        return input[0] - '0';
    } else {
        // Store the last digit
        char last_digit = input[length-1];
        // Convert the last char into its numeric value by subtracting '0'
        int convert_digit = last_digit - '0';
        // Recursive case: remove the last char from the string by moving the null terminator one position to the left
        input[length - 1] = '\0';
        // Return this value plus 10 times the integer value of the new shortened string
        return convert_digit + 10 * convert(input);
    }
}
