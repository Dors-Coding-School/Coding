#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

string replace(string input);

int main(int argc, string argv[])
{
    if(argc != 2){
        printf("Wrong command-line arguments\n");
        return 1;
    }
    string word = argv[1];

    string result = replace(word);

    printf("%s\n", result);
}

string replace(string input){
    string output = input;

    for(int i = 0; i < strlen(input); i++){
        char c = tolower(input[i]);

        switch (c)
        {
            case 'a':
                output[i] = '6';
                break;

            case 'e':
                output[i] = '3';
                break;

            case 'i':
                output[i] = '1';
                break;

            case 'o':
                output[i] = '0';
                break;

            default:
                output[i] = input[i];
                break;
        }
    }

    return output;
}
