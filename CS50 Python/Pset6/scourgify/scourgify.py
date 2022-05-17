import sys
import csv

def main():
    check_command_line_arg()
    output = []
    # Try to open the file
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Create name, last name
                split_name = row['name'].split(",")
                # Add them to dict
                output.append({"first": split_name[1].lstrip(), "last": split_name[0], "house": row['house']})
    # If can't open this means that the file does not exist
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    # Write new csv file
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in output:
            writer.writerow({"first": row['first'], "last": row['last'], "house": row['house']})

def check_command_line_arg():
    #Check how many elements in the command line
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # Check if it is a CSV file
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
