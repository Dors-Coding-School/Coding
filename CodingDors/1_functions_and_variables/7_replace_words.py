# Title: replace_words

"""
Write a Python function that takes three input strings 'a', 'b', and 'c', and returns a new string obtained by replacing all occurrences of the string 'b' in the string 'a' with the string 'c'. For instance, if the string 'a' is 'the quick brown fox jumps over the lazy dog', string 'b' is 'fox', and string 'c' is 'cat', the function should return 'the quick brown cat jumps over the lazy dog'.

replace_words('the quick brown fox jumps over the lazy dog', 'fox', 'cat') -> 'the quick brown cat jumps over the lazy dog'
"""

def replace_words(a: str,b:str,c: str)->str:
    return

# Test your code (copy and past this block of code to test your solution)
print(replace_words('I love Python', 'Python', 'coding'))  # Output: 'I love coding'
print(replace_words('I ate pasta yesterday', 'pasta', 'chocolate'))  # Output: 'I ate chocolate yesterday'
print(replace_words('I love python and python programming', 'python', 'coding'))  # Output: 'I love coding and coding programming'
print(replace_words('I am learning python for data science', 'R', 'python'))  # Output: 'I am learning python for data science'
