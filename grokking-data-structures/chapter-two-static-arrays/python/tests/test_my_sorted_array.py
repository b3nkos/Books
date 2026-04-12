from arrays.sorted_array import SortedArray

def test_delete_by_index():
    array = SortedArray(5)
    array.insert(5)
    array.insert(3)
    array.insert(8)
    array.insert(7)
    array.insert(6)

    array.delete_by_index(3)

    assert array.__len__() == 4

def test_binary_search():
    array = SortedArray(6)
    array.insert(1)
    array.insert(2)
    array.insert(3)
    array.insert(3)
    array.insert(4)
    array.insert(5)

    assert array.binary_search(3) == 2
    assert array.binary_search(4) == 4
    assert array.binary_search(5) == 5

