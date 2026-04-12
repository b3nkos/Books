def _find_smallest_index(arr: list[int]) -> int:
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selection_sort(arr: list[int]) -> list[int]:
    new_arr = []
    copied_arr = list(arr)  # copy array before mutating
    for i in range(len(copied_arr)):
        smallest = _find_smallest_index(copied_arr)
        new_arr.append(copied_arr.pop(smallest))
    return new_arr
