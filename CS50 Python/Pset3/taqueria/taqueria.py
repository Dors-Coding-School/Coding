menu = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

price = 0

while True:
    try:
        item = input("Item: ")
        if item.lower() in menu:
            price += float(menu[item.lower()])
            print("Total: $", end="")
            print("{:.2f}".format(round(price,2)))
    except EOFError:
        print()
        break
