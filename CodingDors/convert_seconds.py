#convert_seconds(24) -> 1440

#convert_seconds(59) -> 3540

#convert_seconds(9) -> 540

def convert_seconds(n: int)->int:
    seconds = n * 60
    return seconds

print(convert_seconds(40))
print(convert_seconds(5))