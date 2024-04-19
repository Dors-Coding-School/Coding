# Get user input
camelCase = input("camelCase: ")

# Create empty string
snake_case = ""

# Loop through every letter
for letter in camelCase:
    if letter.isupper():
        snake_case += "_" + letter.lower()
    else:
        snake_case += letter
        
# Print the output
print("snake_case: " + snake_case)
