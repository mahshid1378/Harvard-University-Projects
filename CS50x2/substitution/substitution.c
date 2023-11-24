#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    bool key = true;

    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    else if (argc == 2 && strlen(argv[1]) == 26)
    {
        for (int i = 0, n = strlen(argv[1]); i < n; i++)
        {
            if (!isalpha(argv[1][i]))
            {
                key = false;
            }
            for (int j = 0; j < i; j++)
            {
                if (argv[1][i] == argv[1][j])
                {
                    key = false;
                }
            }
        }
        if (key == false)
        {
            printf("Key must contain 26 different characters.\n");
            return 1;
        }
        if (key == true)
        {
            string plaintext = get_string("plaintext: ");
            printf("ciphertext: ");
            for (int i = 0, n = strlen(plaintext); i < n; i++)
            {
                if (islower(plaintext[i]))
                {
                    int cipheri = plaintext[i] - 97;
                    printf("%c", tolower(argv[1][cipheri]));
                }
                else if (isupper(plaintext[i]))
                {
                    int cipheri = plaintext[i] - 65;
                    printf("%c", toupper(argv[1][cipheri]));
                }
                else
                {
                    printf("%c", plaintext[i]);
                }
            }
            printf("\n");
            return 0;
        }
    }
    else
    {
        printf("Key must contain 26 different characters.\n");
        return 1;
    }
}