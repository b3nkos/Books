"""Write a recursive function to find the maximum number in a list"""

def find_max(nums: list[int]) -> int:
    if not nums:
        return 0

    max_of_rest = find_max(nums[1:])

    return nums[0] if nums[0] > max_of_rest else max_of_rest
