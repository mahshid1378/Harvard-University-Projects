import sys
import os

def count_lines_of_code(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    code_lines = 0
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            code_lines += 1

    return code_lines

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")

    file_path = sys.argv[1]
    if not file_path.endswith('.py'):
        sys.exit("Not a Python file")

    if not os.path.exists(file_path):
        sys.exit("File does not exist")

    try:
        num_lines = count_lines_of_code(file_path)
        print(f"Number of lines of code: {num_lines}")
    except FileNotFoundError:
        sys.exit()