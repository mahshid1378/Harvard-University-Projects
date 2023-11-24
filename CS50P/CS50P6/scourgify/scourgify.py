import csv
import sys

def clean_data(input_file, output_file):
    try:
        with open(input_file, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)
    except FileNotFoundError:
        sys.exit("Could not read {}".format(input_file))

    cleaned_rows = []
    for row in rows:
        full_name = row['name']
        last_name, first_name = full_name.split(', ')
        house = row['house']
        cleaned_rows.append({'first last': f'{first_name} {last_name}', 'house': house})

    with open(output_file, 'w', newline='') as csv_file:
        fieldnames = ['first last', 'house']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)

# Usage: python scourgify.py input_file output_file
if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit("Too many command-line arguments")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        clean_data(input_file, output_file)