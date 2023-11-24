#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <string.h>

bool isValid(long n, string type);
string getType(long n);
int extract(long n, int place);
int getN(long n);
bool checksum(long n);

int main(void)
{
    string type;
    long n;

    n = get_long("Number: ");
    type = getType(n);

    if (strcmp(type, "INVALID") == 0)
    {
        printf("INVALID\n");
    }
    else
    {
        if (isValid(n, type))
        {
            printf("%s\n", type);
        }
        else
        {
            printf("INVALID\n");
        }
    }
}

bool isValid(long n, string type)
{
    if (strcmp(type, "VISA") == 0 && (getN(n) == 13 || getN(n) == 16))
    {
        return true;
    }
    else if (strcmp(type, "AMEX") == 0 && getN(n) == 15)
    {
        return true;
    }
    else if (strcmp(type, "MASTERCARD") == 0 && getN(n) == 16)
    {
        return true;
    }
    else
    {
        return false;
    }
}

string getType(long n)
{
    if (extract(n, 10) == 4 && checksum(n))
    {
        return "VISA";
    }
    else if ((extract(n, 100) == 34 || extract(n, 100) == 37) && checksum(n))
    {
        return "AMEX";
    }
    else if ((extract(n, 100) >= 51 && extract(n, 100) <= 55) && checksum(n))
    {
        return "MASTERCARD";
    }
    else
    {
        return "INVALID";
    }
}

int extract(long n, int p)
{
    while (n >= p)
    {
        n = n / 10;
    }
    return (int)n;
}

int getN(long n)
{
    return log10(n) + 1;
}

bool checksum(long n)
{
    int sum = 0;
    int num_digits = 0;
    int p = 0;
    long digits = n;

    while (digits > 0)
    {
        if (p == 1)
        {
            int digit = digits % 10;
            digit = digit * 2;
            if (digit > 9)
            {
                digit = digit - 9;
            }
            sum += digit;
        }
        else
        {
            sum += digits % 10;
        }
        digits /= 10;
        num_digits++;
        p = 1 - p;
    }

    if ((sum % 10) == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}