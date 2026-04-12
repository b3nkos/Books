from binary_search import binary_search

def test_binary_search():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search(my_list, 5) == 4

def test_binary_search_not_found():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search(my_list, -77) is None