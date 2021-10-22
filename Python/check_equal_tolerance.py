def check_equal_tolerance(a, b, tol):
    if len(a) != len(b):
        return False

    for i in range(0, len(a)):
        if abs(a[i] - b[i]) >= tol:
            return False

    return True
