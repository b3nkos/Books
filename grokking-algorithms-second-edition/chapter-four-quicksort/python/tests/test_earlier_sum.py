from src.earlier_sum import earlier_sum


def test_sum():
    assert earlier_sum([]) == 0
    assert earlier_sum([5]) == 5
    assert earlier_sum([1, 2, 3]) == 6
    assert earlier_sum([-1, 1]) == 0
    assert earlier_sum([-1, -2]) == -3
    assert earlier_sum([1, -2, 3]) == 2