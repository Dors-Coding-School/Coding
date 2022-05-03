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
# Print the beginning of the output
print("Adieu, adieu, to " + names_list[0], end="")
# Check if there is only one name
if len(names_list) == 1:
    print()
elif len(names_list) == 2:
    print(" and " + names_list[1])
# Loop through names list
else:
    length_of_the_list = len(names_list)
    for i in range(1, length_of_the_list):
        if i == length_of_the_list - 1:
            print(", and " + names_list[i])
        else:
            print(", " + names_list[i], end="")
