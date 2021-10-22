import math


def standardize(data):
    suma = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    sd = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        data[i] = (data[i] - mean) / sd

    return data
