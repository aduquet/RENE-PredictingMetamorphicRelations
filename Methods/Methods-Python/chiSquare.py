def chiSquare(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
