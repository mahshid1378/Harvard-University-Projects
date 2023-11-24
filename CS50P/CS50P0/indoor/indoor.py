def lowercase_input():
    user_input = input("Enter a sentence: ")
    lowercase_sentence = ""
    for char in user_input:
        if char.isalpha():
            lowercase_sentence += char.lower()
        else:
            lowercase_sentence += char
    print("Lowercase sentence:", lowercase_sentence)


lowercase_input()