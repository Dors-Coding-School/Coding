# Title: nested_value

"""
Given a nested dictionary and a list of keys, return the value at the specified depth in the nested dictionary. If any key is not present, return False.

nested_value({'a': {'b': {'c': 1}}}, ['a', 'b', 'c']) -> 1
nested_value({'key': 'value'}, ['key', 'missing']) -> False
nested_value({'fruit': {'apple': {'color': 'red'}}}, ['fruit', 'apple', 'color']) -> 'red'
"""

def nested_value(d, keys):
    return

# Test your code (copy and past this block of code to test your solution)
print(nested_value({'a': {'b': {'c': 1}}}, ['a', 'b', 'c']))  # Output: 1
print(nested_value({'fruit': {'apple': {'color': 'red'}}}, ['fruit', 'apple', 'color']))  # Output: 'red'
print(nested_value({'level1': {'level2': {'level3': 'deep'}}}, ['level1', 'level2']))  # Output: {'level3': 'deep'}
print(nested_value({'first': {'second': {'third': {'fourth': 'value'}}}}, ['first', 'second', 'third', 'fourth']))  # Output: 'value'
print(nested_value({'key': 'value'}, ['key', 'missing']))  # Output: False
print(nested_value({}, ['missing']))  # Output: False
