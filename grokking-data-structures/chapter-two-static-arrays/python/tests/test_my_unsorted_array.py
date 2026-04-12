from src.my_unsorted_array import creating_array
from src.my_unsorted_array import set_array_value
from src.my_unsorted_array import max_in_array
from src.my_unsorted_array import min_in_array
from src.my_unsorted_array import max_and_min_value

def test_creating_array():
    array = creating_array(5)

    assert array.__len__() == 5
    assert array[0] == 0

def test_creating_array_with_value():
    array = set_array_value(5, 55)
    assert array.__len__() == 5
    assert array[0] == 55

def test_max_in_array():
    array = creating_array(3)
    array[0] = 12
    array[1] = 22
    array[2] = 33

    assert max_in_array(array) == (2, 33)

def test_min_in_array():
    array = creating_array(3)
    array[0] = 12
    array[1] = 8
    array[2] = 33

    assert min_in_array(array) == (1, 8)

def test_max_and_min_value():
    array = creating_array(3)
    array[0] = 12
    array[1] = 8
    array[2] = 33

    assert max_and_min_value(array) == (33, 8)