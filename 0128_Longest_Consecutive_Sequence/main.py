# SOLUTION 2
def longestConsecutive(nums: list[int]) -> int:
    if not nums:
        return 0
    nums = set(nums)
    _max = 1
    for num in nums:
        _act = 1
        if num - 1 not in nums:
            new = num + 1
            while new in nums:
                new += 1
                _act += 1
            _max = max(_max, _act)
    return _max


print(longestConsecutive(nums=[1, 2, 3, 5, 11, 12, 13, 14, 15, 16]))


# SOLUTION 1
# def longestConsecutive(nums: list[int]) -> int:
#     if len(nums) == 0:
#         return 0
#     nums.sort()
#     _max = 1
#     _act = 1
#     _ret = nums[0]
#     for num in nums[1:]:
#         if _ret == num:
#             continue
#         if _ret + 1 == num:
#             _act += 1
#             if _act > _max:
#                 _max = _act
#         else:
#             _act = 1
#         _ret = num
#     return _max


