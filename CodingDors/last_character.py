#last_character('hello') -> 'o'

#last_character('world') -> 'd'

#last_character('CodingDors') -> 's'

def last_character(s: str) -> str:
    return s[-1]

print(last_character("world"))