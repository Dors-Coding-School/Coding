# Get user input
answer = input("Input: ")
# Print "Output: "
print("Output: ", end="")
# Loop through every letter
for letter in answer:
    # Check if it is not vowels whether inputted in uppercase or lowercase
    if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        # Print the letter
        print(letter, end="")
print()
