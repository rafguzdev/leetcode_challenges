# SOLUTION 2
def fun(s: str) -> int:
    text = ""
    m = 0
    for c in s:
        if c not in text:
            text += c
        else:
            text = text[text.index(c) + 1:] + c
        m = max(m, len(text))
    return m


print(fun('abcabcd'))

# SOLUTION 1
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
