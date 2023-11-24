def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # Remove the leading $ and convert to float
    amount = float(d[1:])
    return amount

def percent_to_float(p):
    # Remove the % sign and convert to float
    percentage = float(p[:-1]) / 100
    return percentage

main()