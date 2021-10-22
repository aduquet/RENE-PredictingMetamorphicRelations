def weighted_average(a, b):
    sum1 = 0
    sum2 = 0

    for i in range(0, len(a)):
        sum1 += a[i] * b[i]
        sum2 += b[i]

    return sum1 / sum2
