#convert_celsius_to_kelvin(100) -> 373.15

#convert_celsius_to_kelvin(170) -> 443.15

#convert_celsius_to_kelvin(50) -> 323.15

#1 Kelvin = Celsius + 273.15

def convert_celsius_to_kelvin(n: int)->float:
    a = float(n)
    b = a + 273.15
    return b

print(convert_celsius_to_kelvin(100))
print(convert_celsius_to_kelvin(45))