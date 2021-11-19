import numpy as np


def consineDistance(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator
