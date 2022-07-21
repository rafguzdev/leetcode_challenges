# SOLUTION 2
def fun(s, t):
    pairs = {}
    for i, j in zip(s, t):
        if i not in pairs.keys():
            if j in pairs.values():
                return False
            else:
                pairs[i] = j
        else:
            if pairs[i] != j:
                return False
    return True


print(fun('aa', 'vv'))

# SOLUTION 1
# def fun(a, b):
#     pairs = {}
#     for i in range(len(a)):
#         if a[i] not in pairs.keys():
#             if b[i] in pairs.values():
#                 return False
#             else:
#                 pairs[a[i]] = b[i]
#         else:
#             if pairs[a[i]] != b[i]:
#                 return False
#     return True