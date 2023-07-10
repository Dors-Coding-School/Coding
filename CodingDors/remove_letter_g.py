#remove_letter_g('going to the grocery store') -> 'oin to the rocery store'

def remove_letter_g(s: str)->str:
    return s.strip("g")

print(remove_letter_g("good"))