vset = ["a", "e", "i", "o", "u"]

def main():
    a = str(input("Input: ").strip())
    print(f"Output: {shorten(a)}")

def shorten(word):
    output = ""
    for i in word:
        if i.lower() not in vset:
            output += i
    return output

if __name__ == "__main__":
    main()