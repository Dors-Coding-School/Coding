# Get user input
answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

# Print Yes if the user inputs 42 or (case-insensitively) forty-two or forty two
if answer.strip() == "42":
    print("Yes")
elif answer.lower().strip() == "forty-two":
    print("Yes")
elif answer.lower().strip() == "forty two":
    print("Yes")
# Otherwise output No.
else:
    print("No")
