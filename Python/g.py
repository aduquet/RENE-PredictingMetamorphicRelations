import math


def g(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    suma = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = math.log(observed[i] / (ratio * expected[i]))
        else:
            dev = math.log(observed[i] / expected[i])

        suma += observed[i] * dev

    return 2 * suma
