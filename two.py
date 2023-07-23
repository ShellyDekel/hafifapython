import functools

# 2
def sumOfList(numberList: list):
    return functools.reduce(lambda a, b: a + b, numberList, 0)