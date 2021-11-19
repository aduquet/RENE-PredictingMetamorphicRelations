def meanDeviation(elements, mean):
    size = len(elements)

    suma = 0

    for i in range(size-1 , -1, -1):
        suma += abs(elements[i] - mean)

    return suma / size
