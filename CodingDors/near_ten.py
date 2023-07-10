#near_ten(48) → True

#near_ten(55) → True

#near_ten(5) → False

def near_ten(n: int)->bool:
    c = abs(n - 50)
    if c <= 10:
        return True
    else:
        return False
    
print(near_ten(45))
print(near_ten(74))