def calculate_change(payment):
    amount_due = max(0, 50 - payment)
    return amount_due

def main():
    payment = 0
    amount_due = 50
    while payment < 50:
        coin = int(input("Insert Coin:").strip())
        if coin in [5, 10, 25]:
            payment += coin
            amount_due = calculate_change(payment)
            if amount_due > 0:
                print(f"Amount Due: {amount_due}")
        else:
            print(f"Amount Due: {amount_due}")

    print(f"Change Owed: {payment - 50}")

if __name__ == "__main__":
    main()