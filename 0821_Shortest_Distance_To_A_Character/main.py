def shortestToChar(s: str, c: str) -> list[int]:
    out = [0] * len(s)
    pos = []
    offset = 0
    while True:
        index = s.find(c, offset)
        if index == -1:
            break
        pos.append(index)
        offset = index + 1
    for idx, letter in enumerate(s):
        val = min(pos, key=lambda x: abs(x-idx))
        out[idx] = abs(val - idx)

    return out


print(shortestToChar(s="aaab", c="b"))
