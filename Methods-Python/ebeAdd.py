def ebeAdd(a, b):

    if len(a) != len(b):
        return None

    result = a.copy()
    for i in range(0, len(a)):
        result[i] += b[i]

    return result

