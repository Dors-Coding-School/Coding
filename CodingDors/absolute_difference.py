#absolute_difference(4, 8) -> 4

#absolute_difference(10, 25) -> 30

def absolute_difference(a: int, b: int)-> int:
    if abs(a - b) > 10:
        return abs(a - b) * 2
    else:
        return abs(a - b)
    
print(absolute_difference(10, 25))
print(absolute_difference(20, 5))
print(absolute_difference(4, 4))