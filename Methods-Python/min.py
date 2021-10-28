def min(elements):
    size = len(elements)
    mini = elements[size - 1]

    for i in range(size - 1, -1, -1):
        if elements[i] < mini:
            mini = elements[i]

    return mini