
# def fun(s):
#     length = len(s)
#     if length < 2:
#         return length
#     maximum = 0
#     for i in range(length):
#         lon = get_longest(s[i:])
#         if lon > maximum:
#             maximum = lon
#         if length - i <= maximum:
#             return maximum
#     return maximum
#
#
# def get_longest(word):
#     a = ''
#     for letter in word:
#         if letter in a:
#             return len(a)
#         else:
#             a += letter
#     return len(a)

# print(fun('abcdabcde'))

def lengthOfLongestSubstring(s: str) -> int:
    dic = ""
    m = 0
    for c in s:
        if c not in dic:
            dic += c
        else:
            dic = dic[dic.index(c) + 1:] + c
        m = max(m, len(dic))
    return m

print(lengthOfLongestSubstring('abcabcd'))


[1,2,3,4]