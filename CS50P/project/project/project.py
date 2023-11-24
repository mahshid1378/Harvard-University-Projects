import getpass
import re
import json
import sys
import io
import emoji
import datetime

CONTACTS_FILE = "contacts.json"
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    print("Telegram Bot Simulation")
    print("1. Register")
    print("2. Enter the platform")

    choice = input("Enter your choice: ")
    if choice == '1':
        register_user()
    elif choice == '2':
        enter_platform()
    else:
        print("Invalid choice. Please try again.")

def register_user():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    mobile_number = getpass.getpass("Enter your mobile number: ")
    date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
    password = getpass.getpass("Enter your password: ")

    if not name or not surname or not mobile_number or not date_of_birth or not password:
        print("Error: All fields must be filled.")
        return

    if not is_valid_password(password):
        print("Error: Password must have at least 8 characters and contain both uppercase letters and numbers.")
        return

    # Perform registration logic here

    print(f"User {name} {surname} successfully registered.")

color_codes = {
    1: "\033[31m",  # Red
    2: "\033[32m",  # Green
    3: "\033[33m",  # Yellow
    4: "\033[34m",  # Blue
    5: "\033[35m",  # Purple
}

def greet_user(name):
    return f"Hello, {name}! How can I assist you today?"

def calculate_sum(a, b):
    return a + b

def is_even(number):
    return number % 2 == 0

def is_valid_password(password):
    # Password must have at least 8 characters and contain both uppercase letters and numbers
    pattern = r"^(?=.*[A-Z])(?=.*\d).{8,}$"
    return re.match(pattern, password) is not None

def read_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file)
    print("Contacts saved successfully.")

def add_contact(user_name):
    contacts = read_contacts()
    user_contacts = contacts.get(user_name, [])
    while True:
        contact_name = input("Enter contact name (leave empty to stop): ")
        if not contact_name:
            break
        contact_mobile = input("Enter contact mobile number: ")
        user_contacts.append({"name": contact_name, "mobile": contact_mobile})
    contacts[user_name] = user_contacts
    save_contacts(contacts)

    if user_contacts:
        print("Your contacts:")
        for i, contact in enumerate(user_contacts, start=1):
            print(f"{i}. {contact['name']} ({contact['mobile']})")

    contact_index = input("Enter the index of the contact to send a message to: ")
    if contact_index.isdigit():
        contact_index = int(contact_index) - 1
        if 0 <= contact_index < len(user_contacts):
            contact = user_contacts[contact_index]
            message = input("Enter your message: ")
            send_message(contact, message)
        else:
            print("Invalid contact index.")
    else:
        print("Invalid contact index. Please enter a number.")

def choose_color():
    while True:
        print("Color Options:")
        for color_num, ski_code in color_codes.items():
            print(f"{color_num}. {ski_code}This is a colored example.\033[0m")

        color_choice = input("Choose the number of the color for your message: ")
        if color_choice.isdigit():
            color_choice = int(color_choice)
            if color_choice in color_codes:
                return color_choice

        print("Invalid color choice. Please try again.")

def send_message(contact, message):
    # Implement your message sending logic here
    message_with_emoji = emoji.emojize(message)
    print(f"Message sent to {contact['name']} ({contact['mobile']}): {message_with_emoji}")

def enter_platform():
    name = input("Enter your name: ")
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Perform platform entry logic here
    print(f"Welcome to the platform, {name}! Current time: {current_time}")

    messages = []  # List to store user's messages
    while True:
        message = input("Enter your message (leave empty to exit): ")
        if not message:
            break

        color = choose_color()
        send_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        messages.append({"message": message, "color": color, "send_time": send_time})

    print("\nYour messages:")
    for i, message in enumerate(messages, start=1):
        colored_message = colorize_message(message["message"], message["color"])
        print(f"{i}. {colored_message} - {message['send_time']}")

    contacts = read_contacts()
    if name in contacts:
        user_contacts = contacts[name]
        if user_contacts:
            print("Your contacts:")
            for i, contact in enumerate(user_contacts, start=1):
                print(f"{i}. {contact['name']} ({contact['mobile']})")
            contact_index = input("Enter the index of the contact to send a message to: ")
            if contact_index.isdigit():
                contact_index = int(contact_index) - 1
                if 0 <= contact_index < len(user_contacts):
                    contact = user_contacts[contact_index]
                    message = input("Enter your message: ")
                    send_message(contact, message)
                else:
                    print("Invalid contact index.")
            else:
                print("Invalid contact index. Please enter a number.")
        else:
            print("You don't have any contacts.")
            add_contact(name)
    else:
        print("You don't have any contacts.")
        add_contact(name)

def colorize_message(message, color):
    message_ski_code = color_codes.get(color, "")
    date_time_ski_code = "\033[30m"  # Black color code
    reset_code = "\033[0m"  # Reset color code
    send_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    colored_message = f"{message_ski_code}{message}{reset_code}"
    colored_send_time = f"{date_time_ski_code}{send_time}{reset_code}"

    return f"{colored_message} - {colored_send_time}"

enter_platform()

if __name__ == "__main__":
    main()