def main():
    time = input("What time is it? ")

    converted_time = convert(time)

    # breakfast between 7:00 and 8:00
    if (converted_time >= 7 and converted_time <= 8):
        print("breakfast time")

    #  lunch between 12:00 and 13:00
    if (converted_time >= 12 and converted_time <= 13):
        print("lunch time")

    # dinner between 18:00 and 19:00
    if (converted_time >= 18 and converted_time <= 19):
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")

    converted_minutes = int(minutes) / 60

    return int(hours) + converted_minutes


if __name__ == "__main__":
    main()
