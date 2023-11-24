#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Asks for a name
    string n;
    n = get_string("Hi! What's your name? ");

    // Print
    printf("Hello I am happy to see you, %s!\n", n);
}