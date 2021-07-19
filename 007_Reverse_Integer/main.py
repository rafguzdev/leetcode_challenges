
def fun(x):
    neg = False
    if x < 0:
        neg = True
        x *= -1
    x = str(x)
    x = x[::-1]
    x = int(x)
    if neg:
        x *= -1
        if x < -2**31:
            return 0
    else:
        if x > 2**31 + 1:
            return 0
    return x


print(fun(-2147483641))
