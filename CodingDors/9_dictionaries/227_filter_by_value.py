# Title: filter_by_value

"""
Given a dictionary and a value, return a new dictionary containing only the key-value pairs with the given value.

filter_by_value({'a': 1, 'b': 2, 'c': 1}, 1) -> {'a': 1, 'c': 1}
filter_by_value({'apple': 'fruit', 'carrot': 'vegetable', 'banana': 'fruit'}, 'fruit') -> {'apple': 'fruit', 'banana': 'fruit'}
"""

def filter_by_value(d, value):
    return

# Test your code (copy and past this block of code to test your solution)
print(filter_by_value({'a': 1, 'b': 2, 'c': 1}, 1))  # Output: {'a': 1, 'c': 1}
print(filter_by_value({'apple': 'fruit', 'carrot': 'vegetable', 'banana': 'fruit'}, 'fruit'))  # Output: {'apple': 'fruit', 'banana': 'fruit'}
print(filter_by_value({}, 'value'))  # Output: {}
print(filter_by_value({'key1': 'value', 'key2': 'other_value', 'key3': 'value'}, 'value'))  # Output: {'key1': 'value', 'key3': 'value'}
