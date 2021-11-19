def weightedMean(elements, theWeigths):

    size = len(elements)
    suma = 0
    weightSum = 0
    for i in range(size, -1, -1):
        w = theWeigths[i]
        suma += elements[i] * w
        weightSum += w
    return suma / weightSum
