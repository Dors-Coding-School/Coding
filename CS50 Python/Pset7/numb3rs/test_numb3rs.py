from numb3rs import validate

def main():
    test_format()
    test_range()

def test_format():
    assert validate(r'cat') == False
    assert validate(r'127') == False
    assert validate(r'127.0') == False
    assert validate(r'127.0.1') == False
    assert validate(r'127.0.1.2') == True

def test_range():
    assert validate(r'255.255.255.255') == True
    assert validate(r'512.1.1.1') == False
    assert validate(r'1.512.1.1') == False
    assert validate(r'1.1.512.1') == False
    assert validate(r'1.1.1.512') == False

if __name__ == "__main__":
    main()
