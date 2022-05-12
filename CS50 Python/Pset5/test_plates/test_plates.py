from plates import is_valid

def main():
    test_min_max_characters()
    test_starting_with_two_letters()
    test_numbers_in_middle()
    test_first_number_zero()
    test_other_characters()

# Plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
def test_min_max_characters():
    assert is_valid('AB') == True
    assert is_valid('ABCDEF') == True
    assert is_valid('A') == False
    assert is_valid('ABCDEFGH') == False

# Plates must start with at least two letters
def test_starting_with_two_letters():
    assert is_valid('AA') == True
    assert is_valid('A2') == False
    assert is_valid('22') == False

# Numbers cannot be used in the middle of a plate; they must come at the end
def test_numbers_in_middle():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

# The first number used cannot be a ‘0’
def test_first_number_zero():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False

# No periods, spaces, or punctuation marks are allowed
def test_other_characters():
    assert is_valid("PI3.14") == False
    assert is_valid("CS 50") == False
    assert is_valid("Hello!") == False

if __name__ == "__main__":
    main()
