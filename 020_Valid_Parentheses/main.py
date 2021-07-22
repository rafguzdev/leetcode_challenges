
def fun(s):
    stack = ''
    for br in s:
        if stack == '' and br in ')}]':
            return False
        elif br in '({[':
            stack += br
        else:
            last = stack[-1]
            if (br == ')' and last == '(') or (br == '}' and last == '{') or (br == ']' and last == '['):
                stack = stack[:-1]
            else:
                return False
    return stack == ''


print(fun("(){}}{"))
