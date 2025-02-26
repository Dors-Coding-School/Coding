# Title: tea_party

"""
We are having a party with amounts of tea and candy. Return the int outcome of the party encoded as 0=bad, 1=good, or 2=great. A party is good (1) if both tea and candy are at least 5. However, if either tea or candy is at least double the amount of the other one, the party is great (2). However, in all cases, if either tea or candy is less than 5, the party is always bad (0).

tea_party(5, 5) → 1
tea_party(10, 5) → 2
tea_party(4, 5) → 0
"""

def tea_party(tea: int, candy: int) -> int:
    return

# Test your code (copy and past this block of code to test your solution)
print(tea_party((5, 5)))  # Output: 1
print(tea_party((10, 5)))  # Output: 2
print(tea_party((4, 5)))  # Output: 0
print(tea_party((10, 2)))  # Output: 0
print(tea_party((15, 30)))  # Output: 2
