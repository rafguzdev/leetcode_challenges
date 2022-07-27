# SOLUTION 1
def wordBreak(s: str, wordDict: list[str]):

    flag = False

    def deep(part):
        nonlocal flag
        for word in wordDict:
            if flag:
                return True
            size = len(word)
            if part[:size] == word:
                new_part = part[size:]
                if new_part == '':

                    flag = True
                    return True
                else:
                    deep(new_part)
        return False

    deep(s)

    return flag


print(wordBreak(s="aaaaaaa", wordDict=["aaaa", "aaaa"]))

