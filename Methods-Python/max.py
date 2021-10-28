def max(elements):
    size = len(elements)
    mixi = elements[size - 1]

    for i in range(size - 1, -1, -1):
        if elements[i] > mixi:
            mixi = elements[i]

    return mixi
