
def fun(strs):
    le = len(strs)
    if le == 0:
        return ''
    if le == 1:
        return strs[0]
    cl = len(strs[0])
    word = strs[0]  # najkrótsze słowo
    for a in strs[1:]:
        al = len(a)
        if al < cl:
            cl = al
            word = a

    for i in range(cl):
        word = word[0:cl-i]
        ok = True
        for ar in strs:
            if word not in ar[:cl-i]:
                ok = False
                break
        if ok:
            return word
    return ''


print(fun(["l", "flidfdgdsfg", "faighlt"]))
