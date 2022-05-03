import sys
import random

# The documentation for pyfiglet isn’t very clear, but you can use the module as follows
from pyfiglet import Figlet
figlet = Figlet()

# Zero if the user would like to output text in a random font.
if len(sys.argv) == 1:
    isRandom = True
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    isRandom = False
else:
    print("Invalid usage")
    sys.exit(1)

#You can then get a list of available fonts with code like this:
figlet.getFonts()

if isRandom == False:
    try:
        #You can set the font with code like this, wherein f is the font’s name as a str:
        font = figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    #You can set the font with code like this, wherein f is the font’s name as a str:
    font = random.choice(figlet.getFonts())

# Get user input
msg = input("Input: ")

#And you can output text in that font with code like this, wherein s is that text as a str:
output = figlet.renderText(msg)

print("Output: ")
print(output)
