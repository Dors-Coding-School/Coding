while True:
    fuel = input("Fraction: ")
    try:
        numerator, denominator = fuel.split("/")
        new_numerator = int(numerator)
        new_denominator = int(denominator)
        p = new_numerator / new_denominator
        if p <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass
new_p = int(p * 100)
if new_p <= 1:
    print("E")
elif new_p >= 99:
    print("F")
else:
    print(f"{new_p}%")
