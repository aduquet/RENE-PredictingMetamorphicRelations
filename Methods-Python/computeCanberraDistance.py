def computeCanberraDistance(a, b):

    sum = 0

    for i in range(0, len(a)):
        num = abs(a[i] - b[i])
        denom = abs(a[i]) + abs(b[i])
        if num == 0 or denom == 0:
            continue
        sum += num/denom

    return sum
