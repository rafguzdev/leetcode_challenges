def mirror(s):
    return s


def fun(s: str) -> int:
    max = 0
    i = 0
    j = 1
    while True:
        part =




print(fun(")()())"))

# def fun(s: str) -> int:
#     # wstepne parowanie
#     if s == '':
#         return 0
#     if s[-1] == '(':
#         s = s[:-1]
#     tab = []
#     i = 0
#     lnt = len(s)
#     while i < lnt:
#         if i + 1 == lnt:
#             tab.append(s[i])
#             break
#         if s[i] == '(' and s[i + 1] == ')':
#             tab.append(2)
#             i += 1
#         else:
#             tab.append(s[i])
#         i += 1
#     # parowanie
#     i = 0
#     run = True
#     while run:
#         if i == len(tab):
#             run = False
#             break
#         if tab[i] == '(':
#             j = i + 1
#             while True:
#                 if j == len(tab):
#                     run = False
#                     break
#                 if tab[j] == '(':
#                     break
#                 if tab[j] == ')':
#                     tab[j] = 2
#                     tab.pop(i)
#                     i = -1
#                     break
#                 j += 1
#         i += 1
#     # podsumowanie
#
#     max = 0
#     cur = 0
#     lnt = len(tab)
#     for i in range(lnt):
#         if tab[i] == 2:
#             cur += 2
#         else:
#             if cur > max:
#                 max = cur
#             cur = 0
#         if i == lnt - 1 and cur > max:
#             max = cur
#     return max