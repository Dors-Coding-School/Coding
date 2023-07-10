#round_floats(3.141) -> 3.14 

#round_floats(75.123456) -> 75.12

def round_floats(n: float)->float:
    result = round(n, 2)
    return result

print(round_floats(103.555555))
print(round_floats(75.123456))