# Get user input
answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

# Convert word to lowercase and remove whitespaces
answer = answer.lower().strip()

# Print Yes if the user inputs 42 or (case-insensitively) forty-two or forty two
if answer == "42":
    print("Yes")
elif answer == "forty-two":
    print("Yes")
elif answer == "forty two":
    print("Yes")
# Otherwise output No.
else:
    print("No")
