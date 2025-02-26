# Title: concatenate_lists

"""
Write a function that concatenates two given lists.

concatenate_lists([1], [2]) -> [1,2]

concatenate_lists([3,4], [5]) -> [3,4,5]

concatenate_lists([2], [4,6,8]) -> [2,4,6,8]
"""

def concatenate_lists(n1: list, n2: list) -> list:
    return

# Test your code (copy and past this block of code to test your solution)
print(concatenate_lists(([1], [2])))  # Output: [1, 2]
print(concatenate_lists(([3, 4], [5])))  # Output: [3, 4, 5]
print(concatenate_lists(([2], [4, 6, 8])))  # Output: [2, 4, 6, 8]
print(concatenate_lists(([1, 3, 5], [2, 4, 6])))  # Output: [1, 3, 5, 2, 4, 6]
print(concatenate_lists(([], [1, 2, 3])))  # Output: [1, 2, 3]
