#convert_fahrenheit_to_celsius(212) -> 100.0

#convert_fahrenheit_to_celsius(194) -> 90.0

#convert_fahrenheit_to_celsius(302) -> 150.0

#1 Celsius = (Fahrenheit - 32) * 5/9

def convert_fahrenheit_to_celsius(n: float) -> float:
    a = (n - 32) * 5 / 9
    return a

print(convert_fahrenheit_to_celsius(100))
print(convert_fahrenheit_to_celsius(220))