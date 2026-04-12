from arrays.sorted_array import SortedArray


def print_ordered_array():
    array = SortedArray(5)
    array.insert(5)
    array.insert(3)
    array.insert(8)
    array.insert(7)
    array.insert(6)

    array.traverse(print)

if __name__ == '__main__':
    print_ordered_array()