# Title: merge_dictionaries

"""
Given two dictionaries, merge them into a single dictionary. If a key exists in both dictionaries, sum the values.

merge_dictionaries({'a': 5, 'b': 3}, {'a': 2, 'c': 7}) -> {'a': 7, 'b': 3, 'c': 7}
merge_dictionaries({'apple': 10}, {'banana': 5, 'apple': 2}) -> {'apple': 12, 'banana': 5}
"""

def merge_dictionaries(d1, d2):
    return

# Test your code (copy and past this block of code to test your solution)
print(merge_dictionaries({'a': 5, 'b': 3}, {'a': 2, 'c': 7}))  # Output: {'a': 7, 'b': 3, 'c': 7}
print(merge_dictionaries({'apple': 10}, {'banana': 5, 'apple': 2}))  # Output: {'apple': 12, 'banana': 5}
print(merge_dictionaries({}, {'a': 5, 'b': 10}))  # Output: {'a': 5, 'b': 10}
print(merge_dictionaries({'x': 2, 'y': 5}, {'x': 3, 'z': 8}))  # Output: {'x': 5, 'y': 5, 'z': 8}
