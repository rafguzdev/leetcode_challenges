# SOLUTION 1
def average(salary: list[int]) -> float:
    return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)


print(average([1000, 2000, 3000]))
