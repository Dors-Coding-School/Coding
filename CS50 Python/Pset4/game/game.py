import random
import sys

while True:
    try:
        level = int(input("Level: "))
        if level >= 1 and level <= 100:
            break
    except:
        pass

random_number = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess >= 1:
            if guess > random_number:
                print("Too large!")
            elif guess < random_number:
                print("Too small!")
            else:
                print("Just right!")
                break
    except:
        pass
