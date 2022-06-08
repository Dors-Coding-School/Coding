from datetime import date
import sys
import re
import inflect

p = inflect.engine()

def main():
    birthday = input("Date of Birth: ")
    try:
        year, month, day = check_birthday(birthday)
    except:
        sys.exit("Invalid date")
    birthDate = date(int(year), int(month), int(day))
    todayDate = date.today()
    diff = todayDate - birthDate
    total_minutes = diff.days * 24 * 60
    output = p.number_to_words(total_minutes, andword='')
    print(output.capitalize() + " minutes")


def check_birthday(birthday):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birthday):
        year, month, day = birthday.split("-")
        return year, month, day


if __name__ == "__main__":
    main()
