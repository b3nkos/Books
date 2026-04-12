def earlier_sum(nums: list[int]) -> int:
    if not nums:
        return 0
    return nums.pop(0) + earlier_sum(nums)
