def backtrack(num: str, i: int, dct: dict, curr_string: str, ans: list):
    if i == len(num):
        ans.append(curr_string)
        return

    string = dct[int(num[i])]
    for k in range(len(string)):
        curr_string = curr_string + string[k]
        backtrack(num, i+1, dct, curr_string, ans)
        l = len(curr_string)
        curr_string = curr_string[:l-1]
    return ans


def fun(digits: str) -> list:
    dct = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
    ans = []
    curr_string = ""
    ans = backtrack(digits, 0, dct, curr_string, ans)
    return ans


print(fun('23'))
