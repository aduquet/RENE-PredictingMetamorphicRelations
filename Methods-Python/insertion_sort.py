def insertion_sort(arrays):

    for i in range(1, len(len(arrays))):
        j = i

        B = arrays[i]
        while j > 0 and arrays[j - 1] > B:
            arrays[j] = arrays[j - 1]
            j -= 1

        arrays[j] = B

    return arrays
