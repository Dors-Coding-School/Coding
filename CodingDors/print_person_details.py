#print_person_details('Maria', 20) -> 'Maria is 20'

#print_person_details('Gi', 25) -> 'Gi is 25'

def print_person_details(name: str,age: str)->str:
    return name + " is " + age

print(print_person_details("Leo", "23"))
print(print_person_details("Gi", "25"))