#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdint.h>
#include "dictionary.h"

typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;
const unsigned int N = 250000;
unsigned int words = 0;
node *table[N];
node *getNode(const char *key)
{
    node *pNode = malloc(sizeof(node));
    if (pNode == NULL)
    {
        printf("Could not allocate memory for linked list node.\n");
        return pNode;
    }
    strcpy(pNode->word, key);
    pNode->next = NULL;
    return pNode;
}

void insertNode(node **head, const char *key)
{
    node *pNode = getNode(key);
    if (*head != NULL)
    {
        pNode->next = *head;
    }
    *head = pNode;
}

bool load(const char *dictionary)
{
    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL)
    {
        return false;
    }
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }
    char word[LENGTH + 1];
    while (fscanf(dict, "%s", word) != EOF)
    {
        unsigned int key = hash(word);
        node **head = &table[key];
        insertNode(head, word);
        words++;
    }
    fclose(dict);
    return true;
}

unsigned int hash(const char *word)
{
    unsigned int hash = 0;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        hash = (hash << 2) ^ word[i];
    }
    return hash % N;
}

bool check(const char *word)
{
    char copy[strlen(word) + 1];
    strcpy(copy, word);
    char *p = copy;
    for (; *p; ++p)
    {
        *p = tolower(*p);
    }
    unsigned int key = hash(copy);
    node *trav = table[key];

    while (trav != NULL)
    {
        if (strcmp(copy, trav->word) == 0)
        {
            return true;
        }
        trav = trav->next;
    }
    return false;
}

unsigned int size(void)
{
    return words;
}

void unloader(node *node)
{
    if (node->next != NULL)
    {
        unloader(node->next);
    }
    free(node);
}

bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        if (table[i] == NULL)
        {
            continue;
        }
        unloader(table[i]);
    }
    return true;
}