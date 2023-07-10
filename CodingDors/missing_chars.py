#missing_chars('hello', 1, 3) -> 'hlo'

#missing_chars('coding', 0, 4) -> 'odig'

def missing_chars(s: str,a: int,b: int)-> str:
    first = s[0:a]
    middle = s[a+1:b]
    last = s[b+1:]
    return first + middle + last

print(missing_chars("coding", 1, 3))