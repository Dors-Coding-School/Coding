# Create list with the name of all months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
# Loop forever
while True:
    # Get user input
    date = input("Date: ")
    try:
        # Split the date by /
        month, day, year = date.split("/")
        # Check if month is in between of 1 and 12 and day between 1 and 31
        if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break
    except:
        try:
            # Split the date by space
            old_month, old_day, year = date.split(" ")
            # Find the number of the month
            for i in range(len(months)):
                if old_month == months[i]:
                    month = i + 1
            # Remove comma from day variable
            day = old_day.replace(",","")
            # Check if month is in between of 1 and 12 and day between 1 and 31
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
        except:
            # Go to the next line
            print()
            pass

# If month is less than 10, add a 0 before
# If day is less than 10, add a 0 before
# Print the result
print(f"{year}-{int(month):02}-{int(day):02}")
