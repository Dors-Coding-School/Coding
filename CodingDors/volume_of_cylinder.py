#volume_of_cylinder(10, 4) -> 125.6

#volume_of_cylinder(5, 2) -> 15.70

#volume_of_cylinder(7, 4) -> 87.92

#3.14 * (diameter/2)^2 * height

def volume_of_cylinder(height: int, diameter: int)->float:
    volume = 3.14 * (diameter/2) ** 2 * height
    return volume

print(volume_of_cylinder(6, 3))