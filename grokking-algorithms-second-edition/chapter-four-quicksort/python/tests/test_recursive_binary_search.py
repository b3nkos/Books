from src.recursive_binary_search import recursive_binary_search


def test_recursive_binary_search():
    assert recursive_binary_search([], 3) is None
    assert recursive_binary_search([1], 2) is None
    assert recursive_binary_search([3], 3) == 0
    assert recursive_binary_search([1, 2], 2) == 1
    assert recursive_binary_search([1, 2, 3], 3) == 2
    assert recursive_binary_search([1, 2, 3, 4], 4) == 3
    assert recursive_binary_search([1, 2, 3, 4], 8) is None
    assert recursive_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 4
    assert recursive_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -77) is None
