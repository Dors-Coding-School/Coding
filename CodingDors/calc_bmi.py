#calc_bmi(75, 180) -> 23.15

#calc_bmi(90, 190) -> 24.93

#calc_bmi(80, 170) -> 27.68

#weight / (height/100)^2

def calc_bmi(weight: int, height: int)->float:
    a = float(weight)
    b = float(height)
    return a / (b / 100) ** 2

print(calc_bmi(90, 130))
print(calc_bmi(50, 100))