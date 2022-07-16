#SOLUTION 1
def fun(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if not s[i].isalpha() and not s[i].isnumeric():
            i += 1
            continue
        if not s[j].isalpha() and not s[j].isnumeric():
            j -= 1
            continue
        if s[i].lower() == s[j].lower():
            i += 1
            j -= 1
        else:
            return False
    return True


print(fun('ab2a'))
