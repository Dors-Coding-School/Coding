# Title: remove_key

"""
Given a dictionary and a key, return a new dictionary with the specified key removed.

remove_key({'a': 1, 'b': 2, 'c': 3}, 'a') -> {'b': 2, 'c': 3}
remove_key({'apple': 'fruit', 'banana': 'fruit', 'carrot': 'vegetable'}, 'banana') -> {'apple': 'fruit', 'carrot': 'vegetable'}
"""

def remove_key(d, key):
    return

# Test your code (copy and past this block of code to test your solution)
print(remove_key({'a': 1, 'b': 2, 'c': 3}, 'a'))  # Output: {'b': 2, 'c': 3}
print(remove_key({'apple': 'fruit', 'banana': 'fruit', 'carrot': 'vegetable'}, 'banana'))  # Output: {'apple': 'fruit', 'carrot': 'vegetable'}
print(remove_key({'x': 10, 'y': 20, 'z': 30}, 'y'))  # Output: {'x': 10, 'z': 30}
print(remove_key({'key1': 'value1', 'key2': 'value2'}, 'key2'))  # Output: {'key1': 'value1'}
print(remove_key({}, 'missing_key'))  # Output: {}
