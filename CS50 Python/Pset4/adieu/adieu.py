import inflect

p = inflect.engine()

# Create list to keep track of names
names_list = []
# Loop forever
while True:
    try:
        # Get user input
        name = input("Name: ")
        names_list.append(name)
    except EOFError:
        # Create new line and stop the loop
        print()
        break
# Printing using inflect module
output = p.join(names_list)
print("Adieu, adieu, to "+ output)
