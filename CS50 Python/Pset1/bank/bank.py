# Get user input
answer = input("Greeting: ")

fix_answer = answer.lower().strip()

# Check if the answer has 'hello', print $0
if 'hello' in fix_answer:
    print("$0")

# Check if answer starts with 'h', print $20
elif fix_answer[0] == 'h':
    print("$20")

# Otherwise, print $100
else:
    print("$100")
