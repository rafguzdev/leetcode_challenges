# SOLUTION 2
def subtractProductAndSum(n: int) -> int:
    n_sum = 0
    n_mul = 1
    n = str(n)
    for i in n:
        j = int(i)
        n_sum += j
        n_mul *= j
    return n_mul - n_sum


print(subtractProductAndSum(77))

# SOLUTION 1
# def subtractProductAndSum(n: int) -> int:
#     n_sum = 0
#     n_mul = 1
#     while n > 0:
#         unit_digit = n % 10
#         n_sum += unit_digit
#         n_mul *= unit_digit
#         n = n // 10
#     return n_mul - n_sum
