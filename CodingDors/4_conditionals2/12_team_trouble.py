# Title: team_trouble

"""
Suppose we have a team of employees, and the parameters 'employee_a' and 'employee_b' indicate if each employee is present or absent from work. We are in trouble if both employees are absent or if both employees are present. Write a function to return True if we are in trouble.

team_trouble(False, False) → True

team_trouble(True, False) → False

team_trouble(True, True) → True
"""

def team_trouble(employee_a: bool, employee_b: bool)-> bool:
    return

# Test your code (copy and past this block of code to test your solution)
print(team_trouble((False, False)))  # Output: True
print(team_trouble((True, True)))  # Output: True
print(team_trouble((True, False)))  # Output: False
print(team_trouble((False, True)))  # Output: False
