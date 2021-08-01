# return x**n

def myPow(x, n):
    if n == 0: return 1
    if n == 1: return x
    if n == -1: return 1 / x
    if n % 2 == 0:
        return myPow(x, n // 2) ** 2
    return (myPow(x, n // 2) ** 2) * x


print(myPow(2, 10))
