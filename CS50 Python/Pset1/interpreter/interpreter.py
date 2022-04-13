math = input("What do you want to know? ")

x, y, z = math.split(" ")

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

print(round(result,1))
