# Title: check_temperature

"""
Write a function check_temperature(temp) that takes a temperature as input (in Fahrenheit) and returns "Hot" if the temperature is above 80 degrees, "Warm" if the temperature is between 60 and 80 degrees, "Cool" if the temperature is between 40 and 60 degrees, and "Cold" if the temperature is below 40 degrees.

check_temperature(30) -> 'Cold'
check_temperature(40) -> 'Cool'
check_temperature(60) -> 'Warm'
check_temperature(80) -> 'Hot'
"""

def check_temperature(temp: int) -> str:
    return

# Test your code (copy and past this block of code to test your solution)
print(check_temperature(30))  # Output: 'Cold'
print(check_temperature(40))  # Output: 'Cool'
print(check_temperature(60))  # Output: 'Warm'
print(check_temperature(80))  # Output: 'Hot'
print(check_temperature(81))  # Output: 'Hot'
print(check_temperature(39))  # Output: 'Cold'
print(check_temperature(59))  # Output: 'Cool'
print(check_temperature(79))  # Output: 'Warm'
