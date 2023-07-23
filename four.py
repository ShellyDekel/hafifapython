# 4
def eightsAndZerosCounter(lowerBound: int, upperBound: int):
    return sum(map("".join([str(num) for num in range(lowerBound, upperBound + 1)]).count, ["0", "8"]))