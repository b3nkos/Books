from typing import Optional

def binary_search(arr: list[int], value: int) -> Optional[int]:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == value:
            return mid
        elif guess > value:
            high = mid - 1
        else:
            low = mid + 1
    return None