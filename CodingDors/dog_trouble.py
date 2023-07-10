#dog_trouble(True, 5) → True

#dog_trouble(True, 7) → False

#dog_trouble(False, 6) → False

def dog_trouble(barking: bool, hour: int)-> bool:
    if barking == True and (hour <= 6 or hour >= 22):
        return True
    else:
        return False
    
print(dog_trouble(True, 14))
print(dog_trouble(True, 23))
print(dog_trouble(False, 3))