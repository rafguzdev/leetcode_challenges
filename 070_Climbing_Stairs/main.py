# SOLUTION 1
from math import factorial


def fun(n: int) -> int:
    if n < 4:
        return n
    else:
        sum = 1
        twos = n // 2
        for i in range(twos):
            p = n - i - 1
            fr1 = factorial(p)
            fr2 = factorial(i + 1)
            sum += (fr1 / (fr2 * factorial(p - i - 1)))
        return int(sum)


print(fun(4))
