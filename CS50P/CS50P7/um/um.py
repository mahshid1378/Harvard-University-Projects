import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    words = s.split()

    for word in words:
        # Convert the word to lowercase for case-insensitive comparison
        lowercase_word = word.lower()

        # Check if the word is "um" and count it
        if lowercase_word.rstrip('.,?!') == "um":
            count += 1

    return count


if __name__ == "__main__":
    main()