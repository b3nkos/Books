from src.count_number_items import count_items


def test_count():
    assert count_items([]) == 0
    assert count_items([1]) == 1
    assert count_items([1, 2]) == 2
    assert count_items([1, 2, 3]) == 3
    assert count_items([1, 2, 3, 4]) == 4
    assert count_items([1, 2, 3, 4, 5]) == 5
    assert count_items([0, 0, 0, 0, 0, 0]) == 6
