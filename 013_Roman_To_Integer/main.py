
def fun(s):
    dct = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    add = 0
    if s.find('IV') >= 0:
        s = s.replace('IV', '')
        add += 4
    if s.find('IX') >= 0:
        s = s.replace('IX', '')
        add += 9
    if s.find('XL') >= 0:
        s = s.replace('XL', '')
        add += 40
    if s.find('XC') >= 0:
        s = s.replace('XC', '')
        add += 90
    if s.find('CD') >= 0:
        s = s.replace('CD', '')
        add += 400
    if s.find('CM') >= 0:
        s = s.replace('CM', '')
        add += 900
    for letter in s:
        add += dct[letter]
    return add


print(fun('MCMXCIV'))
