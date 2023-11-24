#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include "dictionary.h"
#define ALPHABET_SIZE 27

typedef struct trieNode
{
    struct trieNode *next[ALPHABET_SIZE];
    bool endOfWord;
}

trieNode *getNode(void)
{
    trieNode *pNode = NULL;
    pNode = calloc(1, sizeof(trieNode));
    if (pNode == NULL)
    {
        printf("Could not allocate memory for trie node\n.");
        pNode = NULL;
        return pNode;
    }
    else
    {
        pNode->endOfWord = false;
        for (int i = 0; i < ALPHABET_SIZE; i++)
        {
            pNode->next[i] = NULL;
        }
    }
    return pNode;
}

int words = 0;
void insertNode(trieNode *rootNode, char *key)
{
    int length = strlen(key);
    int index;
    trieNode *trav = rootNode;

    for (int i = 0; i < length; i++)
    {
        if (key[i] == '\'')
        {
            index = ALPHABET_SIZE - 1;
        }
        else
        {
            index = key[i] - 97;
        }

        if (trav->next[index] == NULL)
        {
            trav->next[index] = getNode();
        }
        trav = trav->next[index];
    }
    trav->endOfWord = true;
}

struct trieNode *root;
bool load(const char *dictionary)
{
    root = getNode();
    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL)
    {
        return false;
    }
    char word[LENGTH + 1];

    while (fscanf(dict, "%s", word) != EOF)
    {
        insertNode(root, word);
        words++;
    }
    fclose(dict);
    return true;
}

bool check(const char *word)
{
    int length = strlen(word);
    int index;
    trieNode *trav = root;

    for (int i = 0; i < length; i++)
    {
        if (word[i] == '\'')
        {
            index = ALPHABET_SIZE - 1;
        }
        else
        {
            index = tolower(word[i]) - 97;
        }
        if (trav->next[index] == NULL)
        {
            return false;
        }
        trav = trav->next[index];
    }
    return (trav != NULL && trav->endOfWord);
}

unsigned int size(void)
{
    return words;
}

bool unloader(trieNode *node)
{
    for (int i = 0; i < ALPHABET_SIZE; i++)
    {
        if (node->next[i] != NULL)
        {
            unloader(node->next[i]);
        }
    }
    free(node);
    return true;
}

bool unload(void)
{
   return unloader(root);
}