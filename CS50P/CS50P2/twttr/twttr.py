def remove_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return ''.join([char for char in text if char not in vowels])

user_input = input("Enter a text string: ")
result = remove_vowels(user_input)
print("Result:", result)