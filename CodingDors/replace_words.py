#replace_words('the quick brown fox jumps over the lazy dog', 'fox', 'cat') ->
'the quick brown cat jumps over the lazy dog'

def replace_words(a: str,b:str,c: str)->str:
    jump = a.replace(b, c)
    return jump

print(replace_words("the quick brown fox jumps over the lazy dog", "fox", "cat"))