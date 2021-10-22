def find_min(a):

    mini = a[0]
    for i in range(0, len(a)):
        if a[i] < mini:
            mini = a[i]
    return mini
