def manhattanDistance(p1, p2):

    result = 0

    for i in range(0, len(p1)):
        result += abs(p2[i] - p1[i])

    return result
