# Title: make_ends

"""
Given two lists of integers 'a' and 'b', return a new list length 4 containing the first and last elements from the originals lists. The original list will be length 2 or more.

make_ends([1, 2, 3], [4, 5, 6]) → [1, 3, 4, 6]
make_ends([0, 2, 4], [1, 3, 5]) → [0, 4, 1, 5]
make_ends([7, 4, 6, 2], [-1, 0]) → [7, 2, -1, 0]
"""

def make_ends(a: list, b: list) -> list:
    return

# Test your code (copy and past this block of code to test your solution)
print(make_ends(([1, 2, 3], [4, 5, 6])))  # Output: [1, 3, 4, 6]
print(make_ends(([0, 2, 4], [1, 3, 5])))  # Output: [0, 4, 1, 5]
print(make_ends(([7, 4, 6, 2], [-1, 0])))  # Output: [7, 2, -1, 0]
print(make_ends(([1, 2, 3], [3, 2, 1])))  # Output: [1, 3, 3, 1]
print(make_ends(([2, 4, 6], [6, 4, 2])))  # Output: [2, 6, 6, 2]
