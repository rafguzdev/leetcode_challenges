
def fun(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    tab = [''] * numRows
    idx = 0
    inc = 1
    for letter in s:
        tab[idx] += letter
        if idx == numRows - 1:
            inc = -1
        elif idx == 0:
            inc = 1
        idx += inc
    return ''.join(tab)


print(fun('PAYPALISHIRING', 3))
