# SOLUTION 1
def multiply(num1: str, num2: str) -> str:
    lnum1, lnum2 = len(num1), len(num2)
    nnum1, nnum2 = 0, 0
    for i, num in enumerate(num1):
        nnum1 += (ord(num) - 48) * pow(10, lnum1 - 1 - i)
    for i, num in enumerate(num2):
        nnum2 += (ord(num) - 48) * pow(10, lnum2 - 1 - i)
    return str(nnum1 * nnum2)


print(multiply('0', '34'))
