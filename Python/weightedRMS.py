def weightedRMS(data, weights):

    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts = data[i] * data[i] * weights[i]

    return sumOfProducts / sumOfSquaredProducts
