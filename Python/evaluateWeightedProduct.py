import math


def evaluateWeightedProduct(values, weigths, begin, length):

    product = 1
    for i in range(begin, begin + length):
        product *= math.pow(values[i], weigths[i])

    return product
