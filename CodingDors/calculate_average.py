#calculate_average(5, 10, 15) -> 10.00

#calculate_average(1, 1, 7) -> 3.00

#calculate_average(-1, -5, -9) -> - 3.00

def calculate_average(n1: int, n2: int, n3:int)->float:
    average = (n1 + n2 + n3) / 3
    return average

print(calculate_average(5, 20, 50))

