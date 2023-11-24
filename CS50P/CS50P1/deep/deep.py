def big_questions():
    user_input = input("What is the answer to the big questions of life, the universe, and everything else? ")
    user_input = user_input.strip().lower()

    if user_input == '42' or user_input == 'forty-two' or user_input == 'fortytwo'or user_input == 'forty two'or user_input == 'Forty TwO' or user_input == '42 ' or user_input == ' 42':
        print("Yes")
    else:
        print("No")

big_questions()