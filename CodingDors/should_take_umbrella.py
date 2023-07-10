#should_take_umbrella(False, False) → False

#should_take_umbrella(True, False) → True

#should_take_umbrella(False, True) → False

def should_take_umbrella(is_raining: bool, is_sunny: bool)->bool:
    if is_raining == True or is_sunny == False:
        return True
    else:
        return False
    
print(should_take_umbrella(True, True))
print(should_take_umbrella(False, True))
print(should_take_umbrella(False, False))