# SOLUTION 1
import collections


def hammingWeight(n: int) -> int:
    return collections.Counter(bin(n))['1']


print(hammingWeight(0o00000000000000000000000010000000))
