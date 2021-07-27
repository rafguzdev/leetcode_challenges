
def lengthOfLastWord(s: str) -> int:
    arr = s.split()
    if len(arr) == 0:
        return 0
    else:
        return len(arr[-1])


print(lengthOfLastWord('Hello World'))
