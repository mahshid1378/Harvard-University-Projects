emojicons = {
    ':1st_place_medal:': '🥇',
    ':money_bag:': '💰',
    ':thumbsup:': '👍',
    ':earth_asia:': '🌏',
    ':candy:': '🍬',
    ':ice_cream:': '🍨'
}

def emojize_string(input_str):
    words = input_str.split()
    emojized_words = []

    for word in words:
        if word in emojicons:
            emojized_words.append(emojicons[word])
        else:
            emojized_words.append(word)

    emojized_str = ' '.join(emojized_words)
    return emojized_str

def process_input(input_str):
    processed_str = input_str
    for code, emoji in emojicons.items():
        processed_str = processed_str.replace(code, emoji)
    return processed_str

user_input = input(" ")
processed_input = process_input(user_input)
emojized_output = emojize_string(processed_input)
print(emojized_output)