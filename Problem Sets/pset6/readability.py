from cs50 import get_string

def printGradeLevel(index):
    # print result
    if index < 1:
        print("Before Grade 1")
    elif index > 15:
        print("Grade 16+")
    else:
        print(f"Grade {index}")

def getGradeLevel(numLetters, numSentences, numWords):
    # calculate the coleman liau index
    L = numLetters / numWords * 100
    S = numSentences / numWords * 100
    index = round(0.0588 * L - 0.296 * S - 15.8)
    return index

def getNumLetters(text):
    # loop through text, counting number of letters, words and sentences
    l = 0
    for c in text:
        if c.isalpha():
            l += 1
    return l

def getNumWords(text):
    # loop through text, counting number of letters, words and sentences
    w = 0
    for c in text:
       if c == " ":
          w += 1
    w += 1
    return w

 
def getNumSentences(text):
    # loop through text, counting number of letters, words and sentences
    s = 0
    for c in text:
        if c in [".", "!", "?"]:
            s += 1
    return s

def main():
    # get input from user
    text = get_string("Text: ")

    numLetters = getNumLetters(text);
    numWords  = getNumWords(text);
    numSentences = getNumSentences(text);

    gradeLevel = getGradeLevel(numLetters, numSentences, numWords);

    printGradeLevel(gradeLevel);

main()