def elementwise_max(a, b):

    r = []

    for i in range(0, len(a)):
        if a[i] > b[i]:
            r[i] = a[i]
        else:
            r[i] = b[i]

    return r
