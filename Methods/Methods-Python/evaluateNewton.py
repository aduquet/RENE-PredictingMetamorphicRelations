def evaluateNewton(a, c, z):

    n = len(c) - 1
    value = a[n]

    for i in range(n - 1, -1, -1):
        value = a[i] + (z - c[i]) * value

    return value
