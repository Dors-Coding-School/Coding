#second_character('hello') -> 'e'

#second_character('world') -> 'o'

#second_character('CodingDors') -> 'o'

def second_character(s: str) -> str:
    second = s[1]
    return second

print(second_character("hello"))
print(second_character("father"))