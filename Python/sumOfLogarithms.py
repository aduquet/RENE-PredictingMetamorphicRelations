import math


def sumOfLogarithms(elements):
    logsum = 0

    for i in range(0, len(elements)):
        logsum += math.log(elements[i])

    return logsum
