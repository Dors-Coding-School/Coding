# Title: in_one_to_ten

"""
Given a number n, return True if n is in the range 1..10, inclusive. Unless "outside_mode" is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.

in_one_to_ten(5, True) → True
in_one_to_ten(11, False) → False
in_one_to_ten(1, True) → True
"""

def in_one_to_ten(n: int, outside_mode: bool) -> bool:
    return

# Test your code (copy and past this block of code to test your solution)
print(in_one_to_ten((5, True)))  # Output: True
print(in_one_to_ten((11, False)))  # Output: False
print(in_one_to_ten((1, True)))  # Output: True
print(in_one_to_ten((0, False)))  # Output: False
print(in_one_to_ten((10, True)))  # Output: True
print(in_one_to_ten((20, False)))  # Output: False
print(in_one_to_ten((3, True)))  # Output: True
