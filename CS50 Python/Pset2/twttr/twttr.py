# Get user input
answer = input("Input: ")

# Loop through every letter
for letter in answer:
    # Check if it is not vowels whether inputted in uppercase or lowercase
    if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        no_vowels += letter

print("Output: " + no_vowels)
