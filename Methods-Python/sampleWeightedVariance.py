def sampleWeightedVariance(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
