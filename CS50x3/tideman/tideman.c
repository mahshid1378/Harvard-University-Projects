#include <cs50.h>
#include <stdio.h>
#include <string.h>
#define MAX 9

int preferences[MAX][MAX];
bool locked[MAX][MAX];

typedef struct
{
    int winner;
    int loser;
} pair;
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }
    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    for (int i = 0; i < voter_count; i++)
    {
        int ranks[candidate_count];
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);
            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }
        record_preferences(ranks);
        printf("\n");
    }
    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

bool vote(int rank, string name, int ranks[])
{
    for (int i = 0; i < candidate_count; i++)
        if (strcmp(name, candidates[i]) == 0)
        {
            ranks[rank] = i;
            return true;
        }
    return false;
}

void record_preferences(int ranks[])
{
    for (int i = 0; i < candidate_count - 1; i++)
        for (int j = i + 1; j < candidate_count; j++)
            preferences[ranks[i]][ranks[j]]++;
}
void add_pairs(void)
{
    int winner, loser;
    for (int i = 0; i < candidate_count; i++)
        for (int j = 0; j < candidate_count; j++)
            if (preferences[i][j] > preferences[j][i])
            {
                pairs[pair_count] = (pair){.winner = i, .loser = j};
                pair_count++;
            }
}

void sort_pairs(void)
{
    void swap_pairs(pair * a, pair * b);
    int row, col, next_row, next_col, strength, next_strength;

    for (int i = 0; i < pair_count - 1; i++)
        for (int j = i + 1; j < pair_count; j++)
        {
            row = pairs[i].winner;
            col = pairs[i].loser;
            next_row = pairs[j].winner;
            next_col = pairs[j].loser;
            strength = preferences[col][row] - preferences[row][col];
            next_strength = preferences[next_col][next_row] - preferences[next_row][next_col];

            if (strength > next_strength)
                swap_pairs(&pairs[i], &pairs[j]);
        }
}

void lock_pairs(void)
{
    bool is_cycle(int a, int b);
    for (int i = 0; i < pair_count; i++)
        if (!is_cycle(pairs[i].loser, pairs[i].winner))
            locked[pairs[i].winner][pairs[i].loser] = true;
}

void print_winner(void)
{
    int counter;

    for (int i = 0; i < candidate_count; i++)
    {
        counter = 0;
        for (int j = 0; j < candidate_count; j++)
            if (!locked[j][i])
                counter++;

        if (counter == candidate_count)
        {
            printf("%s\n", candidates[i]);
            return;
        }
    }
}

void swap_pairs(pair *a, pair *b)
{
    pair temp = *a;
    *a = *b;
    *b = temp;
}

bool is_cycle(int a, int b)
{
    if (a == b)
        return true;

    for (int i = 0; i < candidate_count; i++)
        if (locked[a][i] && is_cycle(i, b))
            return true;
    return false;
}