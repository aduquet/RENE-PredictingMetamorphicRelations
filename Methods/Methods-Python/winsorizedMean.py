def winsorizedMean(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
