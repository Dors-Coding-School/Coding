def main():
    # Get user input
    message = input("Input: ")
    # Remove all vowels
    message_without_vowels = shorten(message)
    # Print "Output: "
    print("Output: " + message_without_vowels)


def shorten(word):
    word_without_vowels = ""
    # Loop through every letter
    for letter in word:
        # Check if it is not vowels whether inputted in upper case or lowercase
        if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            # Add the letter
            word_without_vowels += letter
    # Return the new word
    return word_without_vowels


if __name__ == "__main__":
    main()
