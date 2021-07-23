
def fun(haystack, needle):
    if needle == '':
        return 0
    i = -1
    lnt = len(needle)
    for letter in haystack:
        i += 1
        if letter == needle[0]:
            if haystack[i:i+lnt] == needle:
                return i
    return -1


print(fun('lal', 'al'))
