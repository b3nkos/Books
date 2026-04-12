from selection_sort import selection_sort


def test_empty_list():
    """Test with an empty list."""
    assert selection_sort([]) == []


def test_single_element():
    """Test with a single element."""
    assert selection_sort([42]) == [42]


def test_two_elements():
    """Test with two elements."""
    assert selection_sort([2, 1]) == [1, 2]
    assert selection_sort([1, 2]) == [1, 2]


def test_already_sorted():
    """Test with an already sorted list."""
    assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_reverse_sorted():
    """Test with a reverse sorted list."""
    assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_duplicates():
    """Test with duplicate elements."""
    assert selection_sort([3, 1, 3, 1, 3]) == [1, 1, 3, 3, 3]
    assert selection_sort([5, 5, 5, 5]) == [5, 5, 5, 5]


def test_all_same_elements():
    """Test with all identical elements."""
    assert selection_sort([7, 7, 7]) == [7, 7, 7]


def test_negative_numbers():
    """Test with negative numbers."""
    assert selection_sort([-5, -1, -10, -3]) == [-10, -5, -3, -1]
    assert selection_sort([-1, 0, 1, -2, 2]) == [-2, -1, 0, 1, 2]


def test_mixed_positive_negative():
    """Test with mixed positive and negative numbers."""
    assert selection_sort([10, -5, 0, 3, -8]) == [-8, -5, 0, 3, 10]


def test_large_list():
    """Test with a larger list."""
    unsorted = [64, 25, 12, 22, 11, 90, 88, 45, 50, 32]
    expected = [11, 12, 22, 25, 32, 45, 50, 64, 88, 90]
    assert selection_sort(unsorted) == expected
    

