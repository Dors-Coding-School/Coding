#calculate_area_of_circle(5) -> 78.5

#calculate_area_of_circle(2) -> 12.56

#calculate_area_of_circle(9) -> 254.34

#3.14 * radius^2

def calculate_area_of_circle(n: int)->float:
    area = 3.14 * n ** 2
    return area

print(calculate_area_of_circle(12))
print(calculate_area_of_circle(17.50))