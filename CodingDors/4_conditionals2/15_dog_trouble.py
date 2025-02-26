# Title: dog_trouble

"""
We have a playful dog that barks loudly at night. The 'hour' parameter is the current hour time in the range 0...23. We are in trouble if the dog is barking and the hour is before 6 or after 22. Return True if we are in trouble.

dog_trouble(True, 5) → True

dog_trouble(True, 7) → False

dog_trouble(False, 6) → False
"""

def dog_trouble(barking: bool, hour: int)-> bool:
    return

# Test your code (copy and past this block of code to test your solution)
print(dog_trouble((True, 5)))  # Output: True
print(dog_trouble((True, 7)))  # Output: False
print(dog_trouble((False, 4)))  # Output: False
print(dog_trouble((False, 7)))  # Output: False
print(dog_trouble((True, 20)))  # Output: False
print(dog_trouble((True, 21)))  # Output: False
print(dog_trouble((False, 23)))  # Output: False
print(dog_trouble((True, 23)))  # Output: True
