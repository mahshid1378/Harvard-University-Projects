import sys
import os
from tabulate import tabulate

if len(sys.argv) != 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if not filename.endswith('.csv'):
    sys.exit("Not a CSV file")

if not os.path.exists(filename):
    sys.exit("File does not exist")

with open(filename, 'r') as file:
    table_data = [line.strip().split(',') for line in file.readlines()]

table_formatted = tabulate(table_data, headers="firstrow", tablefmt="grid")

print(table_formatted)