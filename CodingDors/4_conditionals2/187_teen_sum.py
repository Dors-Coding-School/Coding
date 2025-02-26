# Title: teen_sum

"""
Given 2 ints, a and b, return their sum. However, "teen" values in the range 13..19 inclusive, are extra lucky. So if either value is a teen, just return 19.

teen_sum(10, 13) → 19 
teen_sum(2, 3) →  5
teen_sum(9, 0) → 9
"""

def teen_sum(a: int, b: int) -> int:
    return

# Test your code (copy and past this block of code to test your solution)
print(teen_sum((10, 13)))  # Output: 19
print(teen_sum((6, 14)))  # Output: 19
print(teen_sum((13, 6)))  # Output: 19
print(teen_sum((15, 2)))  # Output: 19
print(teen_sum((2, 3)))  # Output: 5
print(teen_sum((19, 0)))  # Output: 19
print(teen_sum((9, 0)))  # Output: 9
print(teen_sum((18, 99)))  # Output: 19
