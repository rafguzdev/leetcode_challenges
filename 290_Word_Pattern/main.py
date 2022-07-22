# SOLUTION 1
def fun(pattern, s):
    pairs = {}
    s = s.split()
    if len(pattern) != len(s):
        return False
    for i, j in zip(pattern, s):
        if i not in pairs.keys():
            if j in pairs.values():
                return False
            else:
                pairs[i] = j
        else:
            if pairs[i] != j:
                return False
    return True


print(fun('aaa', 'aa aa aa aa'))
