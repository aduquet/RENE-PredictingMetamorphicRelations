def chebyshevDistance(p1, p2):
    if len(p1) != len(p2):
        print('Error!')
        return -1

    maxDiff = abs(p1[0] - p2[0])
    for i in range(0, len(p1)):
        diff = abs(p1[i] - p2[i])

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
