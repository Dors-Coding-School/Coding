# Title: dict_intersection

"""
Given two dictionaries, return a new dictionary containing the key-value pairs that are present in both dictionaries.

dict_intersection({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 2, 'd': 4}) -> {'a': 1, 'b': 2}
dict_intersection({'apple': 'fruit', 'carrot': 'vegetable'}, {'banana': 'fruit', 'apple': 'fruit'}) -> {'apple': 'fruit'}
"""

def dict_intersection(d1, d2):
    return

# Test your code (copy and past this block of code to test your solution)
print(dict_intersection({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 2, 'd': 4}))  # Output: {'a': 1, 'b': 2}
print(dict_intersection({'apple': 'fruit', 'carrot': 'vegetable'}, {'banana': 'fruit', 'apple': 'fruit'}))  # Output: {'apple': 'fruit'}
print(dict_intersection({'x': 10, 'y': 20, 'z': 30}, {'x': 15, 'y': 20, 'a': 40}))  # Output: {'y': 20}
print(dict_intersection({'key1': 'value1', 'key2': 'value2'}, {'key3': 'value3', 'key4': 'value4'}))  # Output: {}
print(dict_intersection({}, {}))  # Output: {}
