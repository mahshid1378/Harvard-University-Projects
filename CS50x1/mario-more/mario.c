#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h;
    do
    {
        h = get_int("Height: ");
    }
    while (h < 1 || h > 8);

    for (int r = 1; r <= h; r++)
    {
        for (int col2_space = h - r; col2_space > 0; col2_space--)
        {
            printf(" ");
        }

        for (int col = 1; col <= 2; col++)
        {
            for (int col2 = 0; col2 != r; col2++)
            {
                printf("#");
            }
            if (col == 1)
            {
                printf("  ");
            }
        }

        printf("\n");
    }
}