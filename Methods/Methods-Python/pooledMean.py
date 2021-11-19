def pooledMean(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
