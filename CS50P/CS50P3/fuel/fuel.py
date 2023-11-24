import re

def convert_fraction_to_percentage(fraction):
    try:
        numerator, denominator = map(int, fraction.split('/'))

        if denominator == 0:
            return None

        percentage = round(numerator / denominator * 100)

        if percentage <= 1:
            return 'E'
        elif percentage >= 99:
            return 'F'
        else:
            return percentage

    except (ValueError, ZeroDivisionError):
        return None

def is_valid_fraction(fraction):
    pattern = r'^\d+/\d+$'
    match = re.match(pattern, fraction)
    if match is None:
        return False

    numerator, denominator = map(int, fraction.split('/'))
    return denominator != 0

fraction_input = input("Enter a fractional number: ")

while not is_valid_fraction(fraction_input):
    print("Invalid input. Please enter a valid fractional number.")
    fraction_input = input("Enter a fractional number: ")

percentage = convert_fraction_to_percentage(fraction_input)

if percentage is not None:
    if isinstance(percentage, str):
        print(percentage)
    else:
        print(f"{percentage}%")
else:
    print("Invalid input or division by zero occurred.")