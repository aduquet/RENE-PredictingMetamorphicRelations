def min(data):
    size = len(data)

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(size - 1, -1, -1):
        if elements[i] < min:
            min = elements[i]

    return min