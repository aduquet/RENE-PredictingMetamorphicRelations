import math


def power(data, k):

    for i in range(0, len(data)):
        data[i] = math.pow(data[i], k)

    return data