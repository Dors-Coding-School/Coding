#team_trouble(False, False) → True

#team_trouble(True, False) → False

#team_trouble(True, True) → True

def team_trouble(employee_a: bool, employee_b: bool)-> bool:
    if employee_a == True and employee_b == True:
        return True
    elif employee_a == False and employee_b == False:
        return True
    else:
        return False
    
print(team_trouble(True, True))
print(team_trouble(True, False))
print(team_trouble(False, False))