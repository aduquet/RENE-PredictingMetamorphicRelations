def get_array_value(a, k):

    if k - 1 >= len(a) or k - 1 < 0:
        return -100000
    else:
        return a[k-1]
