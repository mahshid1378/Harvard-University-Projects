import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Split the IP address into four parts
    parts = ip.split(".")

    # Check if there are exactly four parts
    if len(parts) != 4:
        return False

    # Check each part of the IP address
    for part in parts:
        # Check if the part is a valid integer
        try:
            num = int(part)
        except ValueError:
            return False

        # Check if the integer is within the valid range
        if num < 0 or num > 255:
            return False

    return True


if __name__ == "__main__":
    main()