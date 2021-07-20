
def fun(height):
    lt = 0
    rt = len(height) - 1
    area = 0
    while rt > lt:
        area = max(min(height[lt], height[rt]) * (rt - lt), area)
        if height[lt] > height[rt]:
            rt -= 1
        else:
            lt += 1
    return area


print(fun([1, 8, 6, 2, 5, 4, 8, 3, 7]))

# def fun(height):
#     lnt = len(height)
#     top = 0
#     area = 0
#     for i in range(lnt):
#         lt = height[i]
#         if lt <= top:
#             continue
#         top = lt
#         for j in range(lnt-1-i):
#             rt = height[lnt-1-j]
#             dist = lnt - 1 - i - j
#             new_area = min(lt, rt) * dist
#             if new_area > area:
#                 area = new_area
#             if rt >= lt:
#                 break
#     return area
