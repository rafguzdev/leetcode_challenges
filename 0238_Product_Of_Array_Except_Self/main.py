# SOLUTION 3
def productExceptSelf(nums: list[int]) -> list[int]:
    if nums.count(0) > 1:
        return [0 for _ in range(len(nums))]
    prefix = [nums[0]]
    postfix = [nums[-1]]
    for idx, num in enumerate(nums[1:]):
        prefix.append(prefix[idx]*num)
    for idx, num in enumerate(nums[::-1][1:]):
        postfix.append(postfix[idx]*num)
    postfix = postfix[::-1]
    out = [postfix[1]]
    size = len(nums)
    for i in range(1, size):
        if i == size - 1:
            out.append(prefix[-2])
        else:
            out.append(prefix[i-1]*postfix[i+1])
    return out


print(productExceptSelf(nums=[1, 2, 3, 4]))


# SOLUTION 1
# def productExceptSelf(nums: list[int]) -> list[int]:
#     isZero = True if 0 in nums else False
#     out = []
#     for idx, num in enumerate(nums):
#         if num != 0 and isZero:
#             out.append(0)
#         else:
#             new = 1
#             for idy, num2 in enumerate(nums):
#                 if idx != idy:
#                     new *= num2
#             out.append(new)
#     return out

# SOLUTION 2
# def productExceptSelf(nums: list[int]) -> list[int]:
#     if nums.count(0) > 1:
#         return [0 for _ in range(len(nums))]
#     isZero = True if 0 in nums else False
#     mul = 1
#     out = []
#     for num in nums:
#         if num != 0:
#             mul *= num
#     for num in nums:
#         if num != 0 and isZero:
#             out.append(0)
#         elif num == 0:
#             out.append(mul)
#         else:
#             out.append(int(mul/num))
#     return out
