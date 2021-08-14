
def groupAnagrams(strs: list) -> list:
    dict = {}
    for i in range(len(strs)):
        l = str(sorted(strs[i]))
        if l in dict:
            dict[l].append(strs[i])
        else:
            dict[l] = [strs[i]]
    strs = []
    for d in dict:
        strs.append(dict[d])
    return strs


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


