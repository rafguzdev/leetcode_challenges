
def fun(num1, num2):
    c = num1 + num2
    c.sort()
    d = len(c)
    if d == 0:
        return 0
    if d % 2 == 0:
        pos = int(d / 2)
        return (c[pos] + c[pos-1]) / 2
    else:
        return c[int(d/2)]


print(fun([1,3, 15], [2]))
