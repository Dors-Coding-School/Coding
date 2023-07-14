#convert_lb_to_kg(10) -> 4.54

#convert_lb_to_kg(180) -> 81.65

#convert_lb_to_kg(220) -> 99.79

#1 kg = lb * 0.453592

def convert_lb_to_kg(lb: int)->float:
    a = float(lb)
    return a * 0.453592

print(convert_lb_to_kg(180))
print(convert_lb_to_kg(220))
