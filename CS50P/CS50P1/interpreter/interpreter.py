def calculate_expression():
    expression = input("Enter an arithmetic expression (formatted as 'z y x'): ")
    z, operator, x = expression.split()

    z = int(z)
    x = int(x)

    if operator == '+':
        result = z + x
    elif operator == '-':
        result = z - x
    elif operator == '*':
        result = z * x
    elif operator == '/':
        if x == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = z / x
    else:
        print("Error: Invalid operator.")
        return

    print(f"Result: {result:.1f}")

calculate_expression()