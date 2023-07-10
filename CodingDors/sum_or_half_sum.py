#sum_or_half_sum(4, 5) -> 9

#sum_or_half_sum(3, 3) -> 3

def sum_or_half_sum(a: int, b: int)-> int:
    if a != b:
        return a + b
    else:
        return a
    
print(sum_or_half_sum(5, 8))
print(sum_or_half_sum(5, 5))
print(sum_or_half_sum(5, 10))