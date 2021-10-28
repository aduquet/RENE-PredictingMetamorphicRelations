def find_max(a):
    max1 = a[0]

    for i in range(0, len(a)):
        if a[i] > max1:
            max1 = a[i]

    return max1
