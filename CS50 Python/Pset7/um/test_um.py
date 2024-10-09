from um import count

def test_upper_lower_case():
    assert count('Um, thanks for the album') == 1
    assert count('Um, thanks, UM, for, um, the album') == 3


def test_word_with_um():
    assert count('yummi') == 0


def test_sourrounded_by_space():
    assert count('Hi um baby') == 1
