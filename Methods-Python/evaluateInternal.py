import math


def evaluateInternal(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value
