
def fun(nums, target):
    for idx, num in enumerate(nums):
        for idy, num2 in enumerate(nums[idx+1:]):
            if num + num2 == target:
                print(num, num2)
                print([idx, nums.index(num2, idx+1)])
                return True


fun(nums=[80, 80, 11, 15, 12, 22, 145], target=160)
