def find_diff(a, b):
    c = []
    for i in range(0, len(a)):
        c[i] = a[i] - b[i]
    return c
