# SOLUTION 2
def sortedSquares(nums: list[int]) -> list[int]:
    l = 0
    r = len(nums) - 1
    new = []
    while l != r:
        if abs(nums[l]) > abs(nums[r]):
            new.append(pow(nums[l], 2))
            l += 1
        else:
            new.append(pow(nums[r], 2))
            r -= 1

    new.append(pow(nums[l], 2))
    return new[::-1]


print(sortedSquares(nums=[-11, 1]))

# SOLUTION 1
# def sortedSquares(nums: list[int]) -> list[int]:
#
#     if len(nums) == 1:
#         return [pow(nums[0], 2)]
#
#     mid = nums[0]
#     idx = 0
#     update = False
#
#     for i, num in enumerate(nums[1:]):
#         if abs(num) < abs(mid):
#             mid = num
#             idx = i
#             update = True
#         if num == 0:
#             break
#
#     if update:
#         idx += 1
#
#     l = idx - 1
#     r = idx + 1
#
#     size = len(nums)
#     new = [pow(mid, 2)]
#
#     while l >= 0 or r < size:
#         if l < 0:
#             new.append(pow(nums[r], 2))
#             r += 1
#         elif r >= size:
#             new.append(pow(nums[l], 2))
#             l -= 1
#         elif abs(nums[l]) > abs(nums[r]):
#             new.append(pow(nums[r], 2))
#             r += 1
#         elif abs(nums[l]) < abs(nums[r]):
#             new.append(pow(nums[l], 2))
#             l -= 1
#         else:
#             val = pow(nums[r], 2)
#             new.append(val)
#             new.append(val)
#             r += 1
#             l -= 1
#
#     return new
