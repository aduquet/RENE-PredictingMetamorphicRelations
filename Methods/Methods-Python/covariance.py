def covariance(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
