from src.quicksort import quick_sort


def test_quick_sort():
    assert quick_sort([]) == []
    assert quick_sort([1]) == [1]
    assert quick_sort([1, 2]) == [1, 2]
    assert quick_sort([1, 3, 2]) == [1, 2, 3]
    assert quick_sort([10, 5, 2, 3]) == [2, 3, 5, 10]
