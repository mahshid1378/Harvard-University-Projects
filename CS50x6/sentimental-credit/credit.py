from cs50 import get_int

def main():
    n = get_int("Number: ")
    type = getType(n)
    if (type == "INVALID"):
        print("INVALID")
    else:
        if (isValid(n, type)):
            print(type)
        else:
            print("INVALID")

def isValid(n, type):
    if (type == "VISA" and (len(str(n)) == 13 or len(str(n)) == 16)):
        return True
    elif (type == "AMEX" and len(str(n)) == 15):
        return True
    elif (type == "MASTERCARD" and len(str(n)) == 16):
        return True
    else:
        return False

def getType(n):
    if (int(str(n)[0]) == 4 and checksum(n)):
        return "VISA"
    elif ((int(str(n)[:2]) == 34 or int(str(n)[:2]) == 37) and checksum(n)):
        return "AMEX"
    elif ((int(str(n)[:2]) >= 51 and int(str(n)[:2]) <= 55) and checksum(n)):
        return "MASTERCARD"
    else:
        return "INVALID"

def checksum(n):
    sum = 0
    for i in range(len(str(n)) - 2, -1, -2):
        sum += int(str(n)[i]) * 2
        if (int(str(n)[i]) * 2 > 9):
            sum += 1
    for i in range(len(str(n)) - 1, -1, -2):
        sum += int(str(n)[i])
    if (sum % 10 == 0):
        return True
    else:
        return False

main()