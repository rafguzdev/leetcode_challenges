# SOLUTION 1
from collections import Counter


def topKFrequent(nums: list[int], k: int) -> list[int]:
    vals = Counter(nums).most_common(k)
    out = [x[0] for x in vals]
    return out


print(topKFrequent(nums=[3, 0, 1, 0], k=1))


# SOLUTION 2
# def topKFrequent(nums: list[int], k: int) -> list[int]:
#     vals = set(nums)
#     count = {}
#     out = []
#     freq = [[] for _ in range(len(nums) + 1)]
#     for val in vals:
#         count[val] = nums.count(val)
#     for n, c in count.items():
#         freq[c].append(n)
#     for v in freq[::-1]:
#         for n in v:
#             if n == 0 or n:
#                 out.append(n)
#             if len(out) == k:
#                 return out
