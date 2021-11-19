import math


def find_magnitude(a):
    sum = 0
    for i in range(0, len(a)):
        sum += a[i] * a[i]
    result = math.sqrt(sum)
    return result