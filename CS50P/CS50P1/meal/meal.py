def convert(time):
    # Split the time string into hours and minutes
    hours, minutes = time.split(':')

    # Convert hours and minutes to integers
    hours = int(hours)
    minutes = int(minutes)

    # Convert the time to a floating-point value representing hours
    time_in_hours = hours + minutes / 60

    return time_in_hours

def main():
    time = input("Enter the time (in 24-hour format, e.g., 07:00): ")
    time_in_hours = convert(time)

    if 07.00 <= time_in_hours < 08.00:
        print("breakfast time")
    elif 12.00 <= time_in_hours <= 13.00:
        print("lunch time")
    elif 18.00 <= time_in_hours < 19.00:
        print("dinner time")

if __name__ == "__main__":
    main()