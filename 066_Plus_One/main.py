
def fun(nums: list):
    text = ''
    for num in nums:
        text += str(num)
    text = int(text) + 1
    text = str(text)
    return [int(i) for i in text]


print(fun([1, 9, 9, 9]))
