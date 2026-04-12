from src.find_the_maximum_number import find_max


def test_find_max():
    assert find_max([]) == 0
    assert find_max([1]) == 1
    assert find_max([1, 2, 9, 4, 6, 7]) == 9
    assert find_max([0, -1, 5, -8]) == 5
