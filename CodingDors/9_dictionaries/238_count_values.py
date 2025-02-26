# Title: count_values

"""
Given a dictionary, return a new dictionary where the keys are the unique values from the input dictionary and the values are the number of occurrences of each unique value.

count_values({'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}) -> 1: 2, 2: 2, 3: 1}
count_values({'apple': 'fruit', 'carrot': 'vegetable', 'banana': 'fruit'}) -> {'fruit': 2, 'vegetable': 1}
"""

def count_values(d):
    return

# Test your code (copy and past this block of code to test your solution)
print(count_values({'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}))  # Output: {1: 2, 2: 2, 3: 1}
print(count_values({'apple': 'fruit', 'carrot': 'vegetable', 'banana': 'fruit'}))  # Output: {'fruit': 2, 'vegetable': 1}
print(count_values({'x': 'red', 'y': 'green', 'z': 'red'}))  # Output: {'red': 2, 'green': 1}
print(count_values({'key1': 'alpha', 'key2': 'beta', 'key3': 'alpha'}))  # Output: {'alpha': 2, 'beta': 1}
print(count_values({}))  # Output: {}
