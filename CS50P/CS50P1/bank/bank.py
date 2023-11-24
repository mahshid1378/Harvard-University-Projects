def welcome_message():
    user_input = input("Please enter a greeting: ")
    user_input = user_input.strip().lower()

    if user_input.startswith("hello"):
        print("$0")
    elif user_input.startswith("h"):
        print("$20")
    else:
        print("$100")

welcome_message()