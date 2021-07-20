
def fun(s):
    l = len(s)
    if l == 1 or s == s[::-1]:
        return s
    sub = 2
    for _ in range(l-2):
        for i in range(sub):
            word = s[i:l-sub+1+i]
            if word == word[::-1]:
                return word
        sub += 1
    return s[0]


print(fun('ABCBA'))
