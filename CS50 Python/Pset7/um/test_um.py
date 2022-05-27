from um import count

def main():
    test_upper_lower_case()
    test_word_with_um()
    test_sourrounded_by_space()


def test_upper_lower_case():
    assert count('Um, thanks for the album') == 1
    assert count('Um, thanks, UM, for, um, the album') == 3


def test_word_with_um():
    assert count('yummi') == 0


def test_sourrounded_by_space():
    assert count('Hi um baby') == 1


if __name__ == "__main__":
    main()
