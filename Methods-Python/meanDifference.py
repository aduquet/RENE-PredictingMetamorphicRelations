def meanDifference(sample1, sample2):
    sumDifference = 0

    for i in range(0, len(sample1)):
        sumDifference += sample1[i] - sample2[i]

    return sumDifference / len(sample1)
