# Get user input
camelCase = input("camelCase: ")

# Print "snake_case: "
print("snake_case: ", end="")

# Loop through every letter
for letter in camelCase:

    # Check if letter is uppercase
    if letter.isupper():

        # Print underscores and the letter in lowercase
        print("_" + letter.lower(), end="")

    # Otherwise, print letter
    else:
        print(letter, end="")
print()
