def evaluateHoners(coefficients, argument):
    n = len(coefficients)
    result = []

    for i in range( n-2, -1, -1):
        result = argument * result + coefficients[i]

    return result
