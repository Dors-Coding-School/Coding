# Title: update_value

"""
Given a dictionary, a key, and a value, update the value associated with the key in the dictionary. If the key does not exist, add the key-value pair to the dictionary.

update_value({}, 'name', 'Gi') -> {'name': 'Gi'}
update_value({'name': 'Gi'}, 'name', 'Leo') -> {'name': 'Leo'}
update_value({'name': 'Gi'}, 'age', 25) -> {'name': 'Gi', 'age': 25}
"""

def update_value(d, key, value):
    return

# Test your code (copy and past this block of code to test your solution)
print(update_value({}, 'name', 'Gi'))  # Output: {'name': 'Gi'}
print(update_value({'name': 'Gi'}, 'name', 'Leo'))  # Output: {'name': 'Leo'}
print(update_value({'name': 'Gi'}, 'age', 25))  # Output: {'name': 'Gi', 'age': 25}
