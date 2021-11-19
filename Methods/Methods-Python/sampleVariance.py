def sampleVariance(elements, mean):
    size = len(elements)
    suma = 0

    for i in range(size, -1, -1):
        delta = elements[i] - mean
        suma += delta * delta

    return suma / (size - 1)
