# Get user input
answer = input("Greeting: ")

# Convert string to lowercase and remove whitespaces
fix_answer = answer.lower().strip()

# Check if the answer starts with 'hello', print $0
if fix_answer.startswith("hello"):
    print("$0")

# Check if answer starts with 'h', print $20
elif fix_answer.startswith('h'):
    print("$20")

# Otherwise, print $100
else:
    print("$100")
