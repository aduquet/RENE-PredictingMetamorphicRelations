def manhattan_dist(a, b):

    suma = 0
    for i in range(0, len(a)):
        suma += abs(a[i] - b[i])

    return suma
