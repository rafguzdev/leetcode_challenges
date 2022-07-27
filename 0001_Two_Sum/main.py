# SOLUTION 1
def fun(nums, target):
    store = {}
    for idx, num in enumerate(nums):
        if target - num in store:
            return [store[target-num], idx]
        elif num not in store:
            store[num] = idx


print(fun(nums=[2, 7, 2, 15, 11], target=26))

# SOLUTION 2
# def fun(nums, target):
#     for idx, num in enumerate(nums):
#         new = target - num
#         idy = nums[idx+1:].index(new) + idx+1 if new in nums[idx+1:] else -1
#         if idy > -1:
#             return [idx, idy]

# SOLUTION 3
# def fun(nums, target):
#     for idx, num in enumerate(nums):
#         for idy, num2 in enumerate(nums[idx + 1:]):
#             if num + num2 == target:
#                 return [idx, nums.index(num2, idx + 1)]
