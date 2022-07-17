# SOLUTION 1
def fun(nums):
    nums.sort()
    i = 0
    size = len(nums)
    while True:
        if i + 1 == size:
            return nums[i]
        if nums[i] != nums[i+1]:
            return nums[i]
        else:
            i += 2


print(fun([1, 5, 1, 0, 0]))
