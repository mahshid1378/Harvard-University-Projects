import random

def guess_number():
    level = 0
    while level <= 0:
        try:
            level = int(input("level: "))
            if level <= 0:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a positive integer.")

    target_number = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess {}: ".format(level)))
            if guess <= 0:
                print("Please enter a positive integer.")
            elif guess < target_number:
                print("Too small!")
            elif guess > target_number:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            print("Please enter a positive integer.")

guess_number()