# Ask user for input
math = input("What do you want to know? ")

# Get numbers and operators from input
x, y, z = math.split(" ")

# Convert strings to float
new_x, new_z = float(x), float(z)

if y == "+":
    result = new_x + new_z
elif y == "-":
    result = new_x - new_z
elif y == "*":
    result = new_x * new_z
elif y == "/" and z != 0:
    result = new_x / new_z
else:
    print("ZeroDivisionError")

# Round the result to only one decimal place
print(round(result,1))
