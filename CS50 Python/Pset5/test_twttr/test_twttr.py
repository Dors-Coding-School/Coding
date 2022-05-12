from twttr import shorten

def main():
    test_letter_cases()
    test_numbers()
    test_punctuation()

def test_letter_cases():
    assert shorten('apple') == 'ppl'
    assert shorten('BANANA') == 'BNN'
    assert shorten('OrAnGe') == 'rnG'

def test_numbers():
    assert shorten('1234') == '1234'

def test_punctuation():
    assert shorten('!?.,') == '!?.,'

if __name__ == "__main__":
    main()
