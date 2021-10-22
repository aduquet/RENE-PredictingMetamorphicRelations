import math


def find_euc_dist(a, b):
    sum = 0

    for i in range(0, len(a)):
        sum += (a[i] - b[i]) * (a[i] - b[i])

    result = math.sqrt(sum)

    return result
