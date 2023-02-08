import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    new_cases = dict()
    previous_cases = dict()

    for row in reader:
        state = row['state']
        date = row['date']
        cases = int(row['cases'])

        if state not in previous_cases:
            previous_cases[state] = cases
            new_cases[state] = []
        else:
            new_case = cases - previous_cases[state]
            previous_cases[state] = cases

            if state not in new_cases:
                new_cases[state] = []
            if len(new_cases[state]) >= 14:
                new_cases[state].pop(0)
            new_cases[state].append(new_case)

    return new_cases


# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    for state in states:
        recent_cases = new_cases[state][7:]
        last_week_cases = new_cases[state][:7]
        avg_recent = round(sum(recent_cases) / 7)
        avg_last_week = round(sum(last_week_cases) / 7)

        diff = avg_recent - avg_last_week

        if diff > 0:
            msg = "an increase"
        else:
            msg = "a decrese"

        try:
            d = diff / avg_last_week
            p = round(d * 100,2)
        except ZeroDivisionError:
            raise ZeroDivisionError

        print(f"{state} had a 7-day average of {avg_recent} and {msg} of {p}%.")

main()

