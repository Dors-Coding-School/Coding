# Title: absolute_difference

"""
Write a Python function that takes two input numbers 'a' and 'b', and returns the absolute difference between them. However, if the absolute difference is greater than 10, the function should return double the absolute difference instead. For instance, if 'a' is 4 and 'b' is 8, the function should return 4. If 'a' is 10 and 'b' is 25, the function should return 30.

absolute_difference(4, 8) -> 4

absolute_difference(10, 25) -> 30
"""

def absolute_difference(a: int, b: int)-> int:
    return

# Test your code (copy and past this block of code to test your solution)
print(absolute_difference((10, 21)))  # Output: 22
print(absolute_difference((21, 10)))  # Output: 22
print(absolute_difference((30, 21)))  # Output: 9
print(absolute_difference((21, 30)))  # Output: 9
print(absolute_difference((21, 21)))  # Output: 0
print(absolute_difference((15, 15)))  # Output: 0
print(absolute_difference((5, 15)))  # Output: 10
print(absolute_difference((15, 5)))  # Output: 10
