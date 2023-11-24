from validators import email


def main():
    email_address = input("Enter an email address: ")

    if is_valid_email(email_address):
        print("Valid")
    else:
        print("Invalid")


def is_valid_email(email_address):
    return email(email_address)


if __name__ == "__main__":
    main()