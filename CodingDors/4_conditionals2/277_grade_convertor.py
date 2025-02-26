# Title: grade_convertor

"""
Write a function grade_convertor(grade) that takes a grade as a percentage (0-100) and returns a string: "Fail" if the grade is less than 40, "Pass" if the grade is between 40 and 60, and "Excellent" if the grade is more than 60.

grade_convertor(30) -> 'Fail'
grade_convertor(40) -> 'Pass'
grade_convertor(60) -> 'Excellent'
"""

def grade_convertor(grade: int) -> str:
    return

# Test your code (copy and past this block of code to test your solution)
print(grade_convertor(30))  # Output: 'Fail'
print(grade_convertor(40))  # Output: 'Pass'
print(grade_convertor(60))  # Output: 'Excellent'
print(grade_convertor(61))  # Output: 'Excellent'
print(grade_convertor(39))  # Output: 'Fail'
print(grade_convertor(59))  # Output: 'Pass'
