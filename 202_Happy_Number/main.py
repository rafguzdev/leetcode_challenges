# SOLUTION 2
def fun(n: int):
    seen = set()
    check = n
    while check not in seen:
        seen.add(check)
        total = 0
        while check > 0:
            unit_digit = check % 10
            total += unit_digit ** 2
            check = check // 10
        if total == 1:
            return True
        check = total
    return False


print(fun(19))

# SOLUTION 1
# def fun(n: int):
#     pos = []
#     merge = str(n)
#     while merge not in pos:
#         pos.append(merge)
#         merge2 = 0
#         for i in merge:
#             merge2 += pow(int(i), 2)
#         if merge2 == 1:
#             return True
#         merge = str(merge2)
#     return False
