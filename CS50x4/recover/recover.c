#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    FILE *input, *output;
    BYTE *buffer = malloc(64 * sizeof(BYTE));
    if (buffer == NULL)
    {
        fprintf(stderr, "malloc failed\n");
        exit(EXIT_FAILURE);
    }
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image.\n");
        exit(EXIT_FAILURE);
    }
    if ((input = fopen(argv[1], "r")) == NULL)
    {
        fprintf(stderr, "Could not open file.\n");
        exit(EXIT_FAILURE);
    }

    int counter = 0;
    char filename[10];
    bool is_open = false;

    while (fread(buffer, sizeof(BYTE), 64, input) == 64)
    {
        if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && ((buffer[3] & 0xf0) == 0xe0))
        {
            if (is_open)
            {
                fclose(output);
                is_open = false;
            }
            sprintf(filename, "%03i.jpg", counter);
            printf("%s\n", filename);
            if ((output = fopen(filename, "w")) == NULL)
            {
                fprintf(stderr, "Could not create file.\n");
                exit(EXIT_FAILURE);
            }

            fwrite(buffer, sizeof(BYTE), 64, output);
            is_open = true;
            counter++;
        }
        else if (is_open)
            fwrite(buffer, sizeof(BYTE), 64, output);
    }

    free(buffer);
    fclose(input);
    fclose(output);
    return EXIT_SUCCESS;
}