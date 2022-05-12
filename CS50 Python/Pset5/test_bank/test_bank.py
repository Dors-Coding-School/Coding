from bank import value

def main():
    test_hello_cases()
    test_starting_with_h()
    test_other_cases()

def test_hello_cases():
    assert value('hello') == 0
    assert value('HELLO') == 0
    assert value('hello, Gi') == 0
    assert value('Hello, Gi') == 0

def test_starting_with_h():
    assert value('hi there!') == 20
    assert value('How are you?') == 20

def test_other_cases():
    assert value("What's up?") == 100
    assert value("good morning!") == 100

if __name__ == "__main__":
    main()
