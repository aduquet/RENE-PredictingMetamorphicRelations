def sequential_search(a, key):
    for i in range(0, len(a)):
        if a[i] == key:
            return i

    return -1
