# Title: should_take_umbrella

"""
The parameter 'is_raining' is True if it is raining, and the parameter 'is_sunny' is True if we have a sunny day. We should take an umbrella if it is not sunny or it is raining. Return True if we should take an umbrella.

should_take_umbrella(False, False) → False

should_take_umbrella(True, False) → True

should_take_umbrella(False, True) → False
"""

def should_take_umbrella(is_raining: bool, is_sunny: bool)->bool:
    return

# Test your code (copy and past this block of code to test your solution)
print(should_take_umbrella((False, False)))  # Output: True
print(should_take_umbrella((True, False)))  # Output: True
print(should_take_umbrella((False, True)))  # Output: False
print(should_take_umbrella((True, True)))  # Output: True
