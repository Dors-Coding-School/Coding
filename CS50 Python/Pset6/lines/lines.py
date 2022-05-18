import sys

def main():
    check_command_line_arg()
    # Try to open the file
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
        file.close()
    # If can't open this means that the file does not exist
    except FileNotFoundError:
        sys.exit("File does not exist")
    # Loop through the lines and check if starts with # or whitespace
    count_lines = 0
    for line in lines:
        if check_comment_or_empty_line(line) == True:
            count_lines += 1
    print(count_lines)

def check_command_line_arg():
    #Check how many elements in the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # Check if it is a Python file
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

def check_comment_or_empty_line(line):
    if line.lstrip().startswith('#'):
        return False
    if line.isspace():
        return False
    return True

if __name__ == "__main__":
    main()
