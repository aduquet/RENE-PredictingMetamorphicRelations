def hamming_dist(a, b):
    cnt = 0
    for i in range(0, len(a)):
        if a[i] != b[i]:
            cnt += 1

    return cnt
