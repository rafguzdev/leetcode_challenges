
def fun(nums, target):
    if target in nums:
        x = nums.index(target)
        i = 1
        lnt = len(nums)
        while True:
            n = x + i
            if n < lnt and nums[n] == target:
                i += 1
            else:
                return [x, x + i - 1]
    else:
        return [-1, -1]


print(fun([5, 5], 5))

# def fun(nums, target):
#     if target in nums:
#         x = nums.index(target)
#         y = nums.count(target)
#         return [x, x + y - 1]
#     else:
#         return [-1, -1]
