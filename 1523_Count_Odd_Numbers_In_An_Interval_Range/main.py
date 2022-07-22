# SOLUTION 1
def countOdds(low: int, high: int) -> int:
    if low % 2 == 0 and high % 2 == 0:
        return (high - low) // 2
    return (high - low) // 2 + 1


print(countOdds(6, 7))
