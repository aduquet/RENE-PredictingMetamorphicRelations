import math


def sampleSkew(size, moment3, sampleVariance):
    n = size
    s = math.sqrt(sampleVariance)
    m3 = moment3 * n
    return n * m3 / ((n - 1) * (n - 2) * s * s * s)
