# Title: missing_chars

"""
Write a Python function that takes a string 's' and two integers 'a' and 'b', and returns a new string where the character at index 'a' and the character at index 'b' have been removed.  For example, if the string 's' is 'hello' and 'a' is 1 and 'b' is 3, the function should return the string 'hlo', where the characters at indices 1 and 3 (i.e. 'e' and 'l') have been removed.

missing_chars('hello', 1, 3) -> 'hlo'

missing_chars('coding', 0, 4) -> 'odig'
"""

def missing_chars(s: str,a: int,b: int)-> str:
    return

# Test your code (copy and past this block of code to test your solution)
print(missing_chars('coding', 0, 1))  # Output: 'ding'
print(missing_chars('coding', 3, 4))  # Output: 'codg'
print(missing_chars('coding', 0, 5))  # Output: 'odin'
print(missing_chars('abcdef', 2, 4))  # Output: 'abdf'
print(missing_chars('hello world', 6, 10))  # Output: 'hello orl'
