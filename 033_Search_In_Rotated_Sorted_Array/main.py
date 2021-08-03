
def search(nums: list, target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        return -1


print(search([4, 5, 6, 7, 0, 1, 2], 3))


# def search(nums: list, target: int) -> int:
#     if target in nums:
#         return nums.index(target)
#     else:
#         return -1
