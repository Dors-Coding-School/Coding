# Title: valid_vanity_plate

"""
Given a string 's', determine if, after the first appearance of a number in the string, there are any letters. For a string to be considered valid, once numbers start appearing, they should not be followed by any letters.

valid_vanity_plate("ABC123") → True
valid_vanity_plate("AB12CD") → False
valid_vanity_plate("A1B2") → False
"""

def valid_vanity_plate(s: str) -> bool:
    return

# Test your code (copy and past this block of code to test your solution)
print(valid_vanity_plate('ABC123'))  # Output: True
print(valid_vanity_plate('A1B2'))  # Output: False
print(valid_vanity_plate('AB12CD'))  # Output: False
print(valid_vanity_plate('Hell5'))  # Output: True
print(valid_vanity_plate('CS50'))  # Output: True
print(valid_vanity_plate('CS50CS'))  # Output: False
