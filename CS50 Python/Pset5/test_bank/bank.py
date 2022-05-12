def main():
    # Get user input
    greeting = input("Greeting: ")
    # Store the result of value function
    value_to_print = value(greeting)
    print(f"${value_to_print}")


def value(greeting):
    # Convert greeting in all lower and without whitespaces
    greeting = greeting.lower().strip()
    # Check if the answer has 'hello', return 0
    if 'hello' in greeting:
        return 0
    # Check if answer starts with 'h', return 20
    elif 'h' == greeting[0]:
        return 20
    # Otherwise, return 100
    else:
        return 100


if __name__ == "__main__":
    main()
