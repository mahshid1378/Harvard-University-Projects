def calculate_calories(fruit):
    # Dictionary mapping fruits to calorie values
    calorie_chart = {
        "Apple": 130,
        "Banana": 96,
        "Grapes": 69,
        "Strawberries": 32,
        "Blueberries": 57,
        "Raspberries": 53,
        "Pineapple": 50,
        "Mango": 60,
        "Peach": 39,
        "Orange": 62,
        "Kiwi": 41,
        "Watermelon": 30,
        "Cantaloupe": 28,
        "Honeydew melon": 36,
        "Cherries": 50,
        "Pomegranate": 83,
        "Pear": 100,
        "Plum": 46,
        "Avocado": 50,
        "Lemon": 29,
        "Kiwifruit": 90,
        "Sweet": 100,
        "Sweet Cherries": 100
    }

    # Convert input to title case for case-insensitive matching
    fruit = fruit.title()

    if fruit in calorie_chart:
        return calorie_chart[fruit]
    else:
        return None

fruit_input = input("Enter a fruit: ")
calories = calculate_calories(fruit_input)

if calories is not None:
    print(f"The number of calories in a portion of {fruit_input} is {calories}.")
else:
    print("")