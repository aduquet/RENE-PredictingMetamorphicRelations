import math


def skew(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)
