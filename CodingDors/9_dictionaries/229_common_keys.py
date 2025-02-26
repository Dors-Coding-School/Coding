# Title: common_keys

"""
Given two dictionaries, return True if at least one of the keys that are present in both dictionaries.

common_keys({'a': 1}, {'a': 2}) -> True
common_keys({'a': 1}, {'b': 2}) -> False
common_keys({'a': 1, 'b': 2}, {'c': 3, 'b': 3}) -> True
"""

def common_keys(d1, d2):
    return

# Test your code (copy and past this block of code to test your solution)
print(common_keys({'a': 1}, {'a': 2}))  # Output: True
print(common_keys({'a': 1}, {'b': 2}))  # Output: False
print(common_keys({'a': 1, 'b': 2}, {'c': 3, 'b': 3}))  # Output: True
print(common_keys({'a': 1, 'b': 2}, {'c': 3, 'd': 3}))  # Output: False
