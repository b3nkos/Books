from typing import Optional


def recursive_binary_search(items: list[int], search_value: int, low=0, high=None) -> Optional[int]:
    if high is None:
        high = len(items) - 1

    if low > high:
        return None

    mid = (low + high) // 2
    guess = items[mid]

    if search_value == guess:
        return mid
    elif search_value > guess:
        low = mid + 1
    elif search_value < guess:
        high = mid - 1

    return recursive_binary_search(items, search_value, low, high)
