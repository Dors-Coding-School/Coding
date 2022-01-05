#include <stdio.h>
#include <cs50.h>
#include <math.h>

int get_num_digits(long);
int sum_every_other_digit(long);
int multiplyBy2_AddDigits(long);
int sum_remaining_digits(long);
bool is_card_valid(long);
bool isValidAmex(long, int);
bool isValidVisa(long, int);
bool isValidMaster(long, int);
void printCardFlag(long, int);

int main(void)
{
    long card_num = get_long("What is your credit card number: ?\n");
    int num_digits = get_num_digits(card_num);
    bool card_valid = is_card_valid(card_num);
    if (card_valid)
    {
        printCardFlag(card_num, num_digits);
    }
    else
    {
        printf("%s", "INVALID\n");
    }
}

bool isValidAmex(long card_num, int num_digits)
{
    int first_two = (card_num / pow(10, 13));
    if ((num_digits == 15) && (first_two == 34 || first_two == 37))
    {
        return true;
    }
    return false;
}

bool isValidMaster(long card_num, int num_digits)
{
    int first_two = (int)(card_num / (pow(10, 14)));
    if ((num_digits == 16) && (first_two > 50 && first_two < 56))
    {
        return true;
    }
    return false;
}
bool isValidVisa(long card_num, int num_digits)
{

    if (num_digits == 13)
    {
        return ((int)(card_num / pow(10, 12)) == 4);
    }
    else if (num_digits == 16)
    {
        return ((int)(card_num / pow(10, 15)) == 4);
    }
    else
    {
        return false;
    }
}

void printCardFlag(long card_num, int num_digits)
{
    if (isValidMaster(card_num, num_digits))
    {
        printf("%s", "MASTERCARD\n");
    }
    else if (isValidVisa(card_num, num_digits))
    {
        printf("%s", "VISA\n");
    }
    else if (isValidAmex(card_num, num_digits))
    {
        printf("%s", "AMEX\n");
    }
    else
    {
        printf("%s", "INVALID\n");
    }
}
bool is_card_valid(long card_num)
{
    int num_digits = get_num_digits(card_num);
    //sum of every other digit multiplied by 2, starting from second-to-last digit
    int digits_sum1 = sum_every_other_digit(card_num);
    //sum of number that were not multiplied
    int digits_sum2 = sum_remaining_digits(card_num);

    int total_sum = digits_sum1 + digits_sum2;

    return ((total_sum % 10) == 0);
}
int get_num_digits(long card_num)
{
    int count = 0;
    while (card_num != 0)
    {
        card_num /= 10;
        count += 1;
    }
    return count;
}

int sum_remaining_digits(long card_num)
{
    int isAlternateDigit = true;
    int sum = 0;
    while (card_num > 0)
    {
        if (isAlternateDigit)
        {
            sum += (card_num % 10);
        }
        isAlternateDigit = !isAlternateDigit;
        card_num /= 10;
    }
    return sum;
}

int sum_every_other_digit(long card_num)
{
    int isAlternateDigit = false;
    int sum = 0;
    while (card_num > 0)
    {
        if (isAlternateDigit)
        {
            sum += multiplyBy2_AddDigits(card_num);
        }
        isAlternateDigit = !isAlternateDigit;
        card_num /= 10;
    }
    return sum;
}

int multiplyBy2_AddDigits(long card_num)
{
    int sumDigits = 0;
    int current = 2 * (card_num % 10);
    while (current != 0)
    {
        sumDigits += (current % 10);
        current /= 10;
    }
    return sumDigits;
}