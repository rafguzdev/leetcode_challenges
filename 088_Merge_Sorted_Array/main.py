# SOLUTION 1
def fun(nums1, m, nums2, n):
    for i in range(m, len(nums1)):
        k = i - m - 1
        nums1[i] = nums2[k]
    nums1.sort()
    print(nums1)

fun(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 3], n=2)
