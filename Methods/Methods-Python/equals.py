def equals(x, y):

    if len(x) != len(y):
        return False

    for i in range(0, len(x)):
        if abs(y[i] - x[i]) > 0.0001:
            return False

    return True
