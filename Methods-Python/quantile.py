def quantile(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 1)
    lhs = int(index)

    delta = index - lhs

    if n == 0:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
