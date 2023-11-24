menu = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

order_total = 0.0

while True:
    try:
        order = input("Enter an item or 'd-control' to end: ").lower()
        if order == 'd-control':
            break

        if order in menu:
            order_total += menu[order]
            print(f"Total: ${order_total:.2f}")
        else:
            print("Invalid item. Please enter a valid menu item.")

    except EOFError:
        break

print(f"Total: ${order_total:.2f}")