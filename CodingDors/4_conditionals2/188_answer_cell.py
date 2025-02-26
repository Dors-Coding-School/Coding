# Title: answer_cell

"""
Your cell phone rings. Return True if you should answer it. Normally you answer, except in the morning you only answer if it is your mom calling. In all cases, if you are asleep, you do not answer.

answer_cell(False, True, True) → False
answer_cell(True, True, True) → False
answer_cell(False, False, False) → True
"""

def answer_cell(is_morning: bool, is_mom: bool, is_asleep: bool) -> bool:
    return

# Test your code (copy and past this block of code to test your solution)
print(answer_cell((False, True, True)))  # Output: False
print(answer_cell((True, True, True)))  # Output: False
print(answer_cell((False, False, False)))  # Output: True
print(answer_cell((True, False, False)))  # Output: False
print(answer_cell((True, True, False)))  # Output: True
print(answer_cell((False, True, False)))  # Output: True
