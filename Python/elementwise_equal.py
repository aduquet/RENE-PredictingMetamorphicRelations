def elementwise_equal(a, b):

    r = []

    for i in range(0, len(a)):
        if a[i] == b[i]:
            r[i] = True
        else:
            r[i] = False

    return r
