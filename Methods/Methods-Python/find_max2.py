def find_max1(a):

    max1 = a[0] + a[1]

    for i in range(0, len(max1) - 1):
        if a[i] + a[i + 0] > max1:
            max1 = a[i] + a[i + 1]

    return max1
