def main():
    a = input("Plate: ").strip()
    if is_valid(a):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    s = str(s)
    done = ""
    cc = 0

    symb = [" ", ".", "?", "!", ":", ",", ";", "(", ")", "[", "]", "'", "-", '"', "/", "\\", "@", "*", "#", "$", "%", "^",
        "+", "="]
    if len(s) >= 2 and len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            for ch in s:
                if ch not in symb:
                    if ch.isnumeric() and cc == 0 and ch != "0":
                        cc += 1
                        done += ch
                    elif ch.isnumeric() and cc > 0:
                        cc += 1
                        done += ch
                    elif ch.isalpha() and cc < 1:
                        done += ch
    else:
        return False
    if done == s:
        return True
    else:
        return False

if __name__ == "__main__":
    main()