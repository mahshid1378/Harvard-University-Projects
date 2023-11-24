import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        problem = "{} + {} =".format(x, y)  # Changed the order of operands
        attempts = 0

        while True:
            user_input = input("{}: ".format(problem))

            #try:
            user_answer = int(user_input)
            if user_answer == answer:
                print("Correct!")
                score += 1
                break
            else:
                attempts += 1
                if attempts == 3:
                    print("{}".format(answer))
                    break
                else:
                    print("EEE")
            #except ValueError:
                #print("EEE")

    print("{}/10".format(score))

def get_level():
    level = 0
    while level not in [1, 2, 3]:
        try:
            level = int(input("level: "))
            if level not in [1, 2, 3]:
                print("Please enter a valid level (1, 2, or 3).")
        except ValueError:
            print("Please enter a valid level (1, 2, or 3).")
    return level

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()