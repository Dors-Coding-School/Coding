#include <cs50.h>
#include <stdio.h>
#include <math.h>

int every_other_digit(long credit_card);
int multiplyAndSum(int last_digit);
int number_of_digits(long credit_card);
bool isValidAmex(long credit_card, int numDigit);
bool isValidMasterCard(long credit_card, int numDigits);
bool isValidVisa(long credit_card, int numDigits);

int main(void)
{
    long credit_card = get_long("Credit Card: ");
    int sum_every_other_digit = every_other_digit(credit_card);
    int numDigits = number_of_digits(credit_card);
    bool amex = isValidAmex(credit_card, numDigits);
    bool master = isValidMasterCard(credit_card, numDigits);
    bool visa = isValidVisa(credit_card, numDigits);
    if (sum_every_other_digit % 10 != 0){
        printf("INVALID\n");
        return 0;
    }
    else if(amex == true){
        printf("AMEX\n");
    }
    else if(master == true){
        printf("MASTERCARD\n");
    }
    else if(visa == true){
        printf("VISA\n");
    }
    else{
        printf("INVALID\n");
        return 0;
    }
}

bool isValidAmex(long credit_card, int numDigits){
    int first_two_digits = credit_card / pow(10, 13);
    if((numDigits == 15) && (first_two_digits == 34 || first_two_digits == 37)){
        return true;
    }
    else{
        return false;
    }
}

bool isValidVisa(long credit_card, int numDigits){
    if(numDigits == 13){
        int first_digit = credit_card / pow(10, 12);
        if(first_digit == 4){
            return true;
        }
    }
    else if(numDigits == 16){
        int first_digit = credit_card / pow(10, 15);
        if(first_digit == 4){
            return true;
        }
    }
    return false;
}

bool isValidMasterCard(long credit_card, int numDigits){
    int first_two_digits = credit_card / pow(10, 14);
    if((numDigits == 16) && (first_two_digits > 50 && first_two_digits < 56)){
        return true;
    }
    else{
        return false;
    }
}

int number_of_digits(long credit_card){
    int count = 0;
    while(credit_card > 0){
        count = count + 1;
        credit_card = credit_card / 10;
    }
    return count;
}

int every_other_digit(long credit_card){
    int sum = 0;
    bool isAlternateDigit = false;
    while(credit_card > 0){
        if(isAlternateDigit == true){
            int last_digit = credit_card % 10;
            int product = multiplyAndSum(last_digit);
            sum = sum + product;
        }
        else{
            int last_digit = credit_card % 10;
            sum = sum + last_digit;
        }
        isAlternateDigit = !isAlternateDigit;
        credit_card = credit_card / 10;
    }
    return sum;
}

int multiplyAndSum(int last_digit){
    int multiply = last_digit * 2;
    int sum = 0;
    while(multiply > 0){
        int last_digit_multiply = multiply % 10;
        sum = sum + last_digit_multiply;
        multiply = multiply / 10;
    }
    return sum;
}
