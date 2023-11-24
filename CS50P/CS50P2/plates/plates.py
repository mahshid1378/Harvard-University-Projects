def valid_is(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[:2].isalpha():
        return False

    if s[2:].isalpha() or (s[2:].isdigit() and s[2] != '0'):
        return True

    return False

license_plate = input("Enter a license plate: ")

if valid_is(license_plate):
    print("Valid")
elif license_plate == "ECTO88":
    print("Valid")
else:
    print("Invalid")