from arrays.core import Array

def creating_array(n:int) -> Array:
    array = Array(n)
    return array

def set_array_value(n: int, value: int) -> Array:
    array = Array(n)
    array[0] = value
    return array

def max_in_array(array: Array) -> tuple[int, int]:
    if len(array) == 0:
        raise Exception('Max of an empty array')
    max_index = 0
    for index in range(1, len(array)):
        if array[index] > array[max_index]:
            max_index = index

    return max_index, array[max_index]

def min_in_array(array: Array) -> tuple[int, int]:
    if len(array) == 0:
        raise Exception('Max of an empty array')
    min_index = 0
    for index in range(1, len(array)):
        if array[index] < array[min_index]:
            min_index = index

    return min_index, array[min_index]

def max_and_min_value(array: Array) -> tuple[int, int]:
    _, max_value = max_in_array(array)
    _, min_value = min_in_array(array)
    return max_value, min_value
