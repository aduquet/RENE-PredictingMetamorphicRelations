def distance1(p1, p2):

    suma = 0
    for i in range(0, len(p1)):
        suma += abs(p1[i] - p2[i])

    return suma