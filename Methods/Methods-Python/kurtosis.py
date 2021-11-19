import math


def kurtosis(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)
