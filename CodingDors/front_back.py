#front_back('code') → 'eodc'

#front_back('a') → 'a'

def front_back(s: str)-> str:
    first = s[0]
    last = s[-1]
    middle = s[1:-1]
    return last + middle + first

print(front_back("code"))