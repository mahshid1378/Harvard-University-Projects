import datetime

months = [
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

valid_formats = ["%m/%d/%Y", "%d %B %Y", "%B %d, %Y"]

while True:
    date_input = input(" ")

    try:
        # Attempt to parse the date using the first format (month-day-year)
        date = datetime.datetime.strptime(date_input, valid_formats[0])
        break
    except ValueError:
        try:
            # Attempt to parse the date using the second format (day month year)
            date = datetime.datetime.strptime(date_input, valid_formats[1])
            break
        except ValueError:
            try:
                # Attempt to parse the date using the third format (month day, year)
                date = datetime.datetime.strptime(date_input, valid_formats[2])
                break
            except ValueError:
                print("Invalid date format. Please try again.")

formatted_date = date.strftime("%Y-%m-%d")
print(formatted_date)