# SOLUTION 1
def longestCommonPrefix(strs: list[str]) -> str:
    pref = strs[0]
    size = len(strs) - 1
    for word in strs[1:]:
        if len(word) < len(pref):
            pref = word
    while pref != '':
        pref_len = len(pref)
        for idx, word in enumerate(strs):
            compare = word[:pref_len]
            if pref != compare:
                pref = pref[:-1]
                break
            if idx == size:
                return pref
    return ''


print(longestCommonPrefix(["fl", "flidfdgdsfg", "flaighlt"]))

# SOLUTION 2
# def longestCommonPrefix(strs):
#     le = len(strs)
#     if le == 0:
#         return ''
#     if le == 1:
#         return strs[0]
#     cl = len(strs[0])
#     word = strs[0]
#     for a in strs[1:]:
#         al = len(a)
#         if al < cl:
#             cl = al
#             word = a
#
#     for i in range(cl):
#         word = word[0:cl-i]
#         ok = True
#         for ar in strs:
#             if word not in ar[:cl-i]:
#                 ok = False
#                 break
#         if ok:
#             return word
#     return ''
