#remove_whitespace("     hi there") -> "hi there" 

#remove_whitespace("hello world       ") -> "hello world"

def remove_whitespace(s: str)->str:
    result = s.strip()
    return result

print(remove_whitespace("    hey    "))
print(remove_whitespace("leo    "))
print(remove_whitespace("hello world       "))