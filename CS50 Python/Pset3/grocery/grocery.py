grocery = {}

while True:
    try:
        item = input()
        if item.lower() in grocery:
            grocery[item.lower()] += 1
        else:
            grocery[item.lower()] = 1
    except EOFError:
        for key in sorted(grocery.keys()):
            print(grocery[key], key.upper())
        break
