def varianceDifference(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
