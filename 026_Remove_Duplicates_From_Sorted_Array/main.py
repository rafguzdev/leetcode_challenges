
def fun(nums):
    nums[:] = sorted(list(set(nums)))
    return len(nums)


print(fun([1, 1, 2]))
