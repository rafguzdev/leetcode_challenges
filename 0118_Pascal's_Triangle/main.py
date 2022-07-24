# SOLUTION 1
def generate(numRows: int) -> list[list[int]]:
    gen = [[1]]
    for i in range(numRows - 1):
        size = len(gen)
        temp = [1]
        for j in range(size):
            if j == size - 1:
                temp.append(1)
            else:
                temp.append(gen[i][j] + gen[i][j+1])
        gen.append(temp)
    return gen


print(generate(5))
