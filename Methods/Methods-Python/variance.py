def variance(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
