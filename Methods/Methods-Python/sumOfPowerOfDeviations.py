import math


def sumOfPowerOfDeviations(data, k, c):
    suma = 0
    for i in range(0, len(data)):
        suma += math.pow( data[i] - c, k)

    return suma
