# Title: repeat_list

"""
Write a function that repeats a given list n times.

repeat_list([1,2], 3) -> [1,2,1,2,1,2]

repeat_list([5,6,7]], 2) -> [5,6,7,5,6,7]

repeat_list([1], 5) -> [1,1,1,1,1]
"""

def repeat_list(l: list, n: int) -> list:
    return

# Test your code (copy and past this block of code to test your solution)
print(repeat_list(([1, 2], 3)))  # Output: [1, 2, 1, 2, 1, 2]
print(repeat_list(([5, 6, 7], 2)))  # Output: [5, 6, 7, 5, 6, 7]
print(repeat_list(([1], 5)))  # Output: [1, 1, 1, 1, 1]
print(repeat_list(([1, 2, 3, 4], 2)))  # Output: [1, 2, 3, 4, 1, 2, 3, 4]
print(repeat_list(([], 3)))  # Output: []
