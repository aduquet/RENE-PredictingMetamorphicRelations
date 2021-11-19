def check_equal(a, b):

    if len(a) != len(b):
        return False

    for i in range(0, len(a)):
        if a[i] != b[i]:
            return False

    return True
