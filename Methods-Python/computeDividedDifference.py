def computeDividedDifference(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, n):
        for j in range(0, n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
