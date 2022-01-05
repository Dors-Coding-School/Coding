#include <cs50.h>
#include <stdio.h>
#include <math.h>


int main(void)
{
    float change;

    do
    {
    change = round(get_float("Input your change: ") * 100);

    }
    while (change < 0);

    int count = 0;

    while (change >= 25)
    {
        count++;
        change = change - 25;
    }

    while (change >= 10)
    {
        count++;
        change = change - 10;
    }

    while (change >= 5)
    {
        count++;
        change = change - 5;
    }

    while (change >= 1)
    {
        count++;
        change = change - 1;
    }

    printf("%i\n", count);
}