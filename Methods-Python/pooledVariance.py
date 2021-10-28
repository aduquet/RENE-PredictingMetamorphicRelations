def pooledVariance(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
