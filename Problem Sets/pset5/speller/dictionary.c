// Implements a dictionary's functionality

#include <stdbool.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdio.h>
#include <strings.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 26;

unsigned int numWords = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int hashNum = hash(word);

    node *cursor = table[hashNum];
    while(cursor != NULL){
        if (strcasecmp(cursor->word, word) == 0){
            return true;
        }

        cursor = cursor->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    char firstLetter = toupper(word[0]);

    return ((int) firstLetter) - ((int) 'A');
}

// ./speller texts/lalaland.txt
// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    FILE *dictFile = fopen(dictionary, "r");
    //./speller dictionaries/small cat.txt


    if (dictFile == NULL){
        return false;
    }

    char str[LENGTH + 1];
    while (fscanf(dictFile, "%s", str) != EOF){

        node *temp = malloc(sizeof(node));
        if (temp == NULL){
            return false;
        }

        int hashNum = hash(str);

        strncpy(temp->word, str, sizeof(str));

        if (table[hashNum] == NULL)
        {
            temp->next = NULL;
        }
        else
        {
            temp->next = table[hashNum];
        }
        table[hashNum] = temp;
        numWords += 1;
    }

    fclose(dictFile);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return numWords;
}

void freenode(node*n){
    if(n->next != NULL)
    {
        freenode(n->next);
    }
    free(n);
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int k = 0; k<N; k++){
        if (table[k] != NULL){
            freenode(table[k]);
        }
    }
    return true;
}