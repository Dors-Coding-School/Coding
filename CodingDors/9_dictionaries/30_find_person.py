# Title: find_person

"""
Given a dictionary 'd' and a string 'name', return True if the given name exist in our dictionary. Otherwise, False. 

find_person({'Gi': 123, 'Leo': 456}, 'Gi') -> True 

find_person({'Gi': 123, 'Leo': 456}, 'Ana') -> False
"""

def find_person(d: dict,name: str) -> bool:
    return

# Test your code (copy and past this block of code to test your solution)
print(find_person({'Gi': 123, 'Leo': 456}, 'Gi'))  # Output: True
print(find_person({'Gi': 123, 'Leo': 456}, 'Ana'))  # Output: False
print(find_person({}, 'name'))  # Output: False
print(find_person({'name': 'John'}, 'Name'))  # Output: False
print(find_person({'name': 'John'}, 'name'))  # Output: True
