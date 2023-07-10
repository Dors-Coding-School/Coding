#first_character('hello') -> 'h'

#first_character('world') -> 'w'

#first_character('CodingDors') -> 'C'

def first_character(s: str) -> str:
    first = s[0]
    return first

print(first_character("hi"))
print(first_character("world"))