
def maxSubArray(nums: list) -> int:
    maxi = max(nums)
    if maxi < 0:
        return maxi
    out = 0
    plus = 0
    minus = 0
    check = False
    for num in nums:
        if num < 0:
            minus += num
            check = True
        elif num > 0:
            if check:
                dif = plus + minus
                if dif < 0:
                    plus = 0
                    minus = 0
                check = False
            plus = plus + num + minus
            out = max(out, plus)
            minus = 0
    return out


print(maxSubArray([5,4,-1,7,8]))

# ans = nums[0]
# subarr_sum = nums[0]
#
# for i in range(1, len(nums)):
#     subarr_sum = max(nums[i], nums[i] + subarr_sum)
#     ans = max(ans, subarr_sum)
#
# return ans