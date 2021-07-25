
def fun(nums, target):
    if len(nums) < 4:
        return []
    nums.sort()
    ans = []
    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            l, r = j + 1, len(nums) - 1
            while l < r:
                p = nums[i] + nums[j] + nums[l] + nums[r]
                if p == target:
                    ans += [nums[i], nums[j], nums[l], nums[r]],
                    l += 1
                    r -= 1
                elif p < target:
                    l += 1
                else:
                    r -= 1
    return set(tuple(p) for p in ans)


print(fun([-5,5,4,-3,0,0,4,-2], 4))


# def fun(nums, target):
#     lnt = len(nums)
#     if lnt < 4:
#         return []
#     nums.sort()
#     a, b, c = 0, 1, 2
#     out = []
#     while True:
#         suma = nums[a] + nums[b] + nums[c]
#         last = target - suma
#         if last in nums[c + 1:]:
#             new = [nums[a], nums[b], nums[c], last]
#             if new not in out:
#                 out.append(new)
#         c += 1
#         if c > lnt - 2:
#             c = b + 2
#             b += 1
#             if b > lnt - 3:
#                 b = a + 2
#                 c = b + 1
#                 a += 1
#                 if a > lnt - 4:
#                     break
#     return out
