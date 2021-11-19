def lag1(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1

