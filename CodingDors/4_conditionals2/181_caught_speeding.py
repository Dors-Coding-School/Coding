# Title: caught_speeding

"""
You are driving a little too fast, and a police officer stops you. Write a function to return the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. 

If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(100, True) → 2
"""

def caught_speeding(speed: int, is_birthday: bool) -> int:
    return

# Test your code (copy and past this block of code to test your solution)
print(caught_speeding((60, False)))  # Output: 0
print(caught_speeding((65, False)))  # Output: 1
print(caught_speeding((85, False)))  # Output: 2
print(caught_speeding((60, True)))  # Output: 0
print(caught_speeding((65, True)))  # Output: 0
print(caught_speeding((85, True)))  # Output: 1
print(caught_speeding((100, True)))  # Output: 2
