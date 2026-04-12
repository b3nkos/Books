"""Write a recursive function to count the number of items in a list."""

def count_items(items: list[int]) -> int:
    """Count the number of items in a list."""
    if not items:
        return 0

    return 1 + count_items(items[1:])