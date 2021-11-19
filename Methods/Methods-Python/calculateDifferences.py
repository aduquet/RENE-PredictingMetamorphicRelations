def calculateDifferences(x, y):
    z = []

    for i in range(0, len(x)):
        z.append(y[i] - x[i])

    return z
