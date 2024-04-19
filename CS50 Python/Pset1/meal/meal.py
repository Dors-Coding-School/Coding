def main():
    # Ask user for time
    time = input("What time is it? ")

    # Call function convert
    converted_time = convert(time)

    # Breakfast between 7:00 and 8:00
    if (converted_time >= 7 and converted_time <= 8):
        print("breakfast time")

    # Lunch between 12:00 and 13:00
    if (converted_time >= 12 and converted_time <= 13):
        print("lunch time")

    # Dinner between 18:00 and 19:00
    if (converted_time >= 18 and converted_time <= 19):
        print("dinner time")

def convert(time):
    # Create 2 variables to store hours and minutes
    hours, minutes = time.split(":")

    # Convert minutes into a number between 0 and 1
    converted_minutes = int(minutes) / 60

    # Return the converted value to line 6
    return int(hours) + converted_minutes


if __name__ == "__main__":
    main()
