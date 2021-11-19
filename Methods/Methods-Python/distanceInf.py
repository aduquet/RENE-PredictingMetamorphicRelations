import numpy as np


def distanceInf(p1, p2):
    max = 0
    for i in range(0, len(p1)):
        max = np.maximum(max, abs(p1[i] - p2[i]))

    return max
