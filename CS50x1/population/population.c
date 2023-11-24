#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int s;
    do
    {
        s = get_int("Start size: ");
    }
    while (s < 9);

    int e;
    do
    {
        e = get_int("End size: ");
    }
    while (e < s);

    int n = 0;
    int current = s;
    while (current < e)
    {
        current += (current / 3) - (current / 4);
        n++;
    }

    printf("Years: %i\n", n);
}