def harmonicMean(data):
    sumOfInversions = 0
    for i in range(0, len(data)):
        sumOfInversions += 1 / data[i]

    return len(data) / sumOfInversions


