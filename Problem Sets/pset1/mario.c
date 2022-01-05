#include <cs50.h>
#include <stdio.h>

void printLeft(int, int);
void printRight(int);
void nextLine(void);
void printDoubleSpace(void);

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (!(height > 0 && height < 9));

    for (int i = 1; i <= height; i++)
    {
        printLeft(height - i, i);
        printDoubleSpace();
        printRight(i);
        nextLine();
    }
}

void nextLine(void)
{
    printf("\n");
}
void printLeft(int numSpaces, int numHashes)
{
    for (int i = 1; i <= numSpaces; i++)
    {
        printf(" ");
    }
    for (int j = 1; j <= numHashes; j++)
    {
        printf("#");
    }
}

void printRight(int numHashes)
{
    for (int i = 1; i <= numHashes; i++)
    {
        printf("#");
    }
}

void printDoubleSpace(void)
{
    printf(" ");
    printf(" ");
}