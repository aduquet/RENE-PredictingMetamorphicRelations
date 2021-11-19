def count_k(a, k):
    cnt = 0
    for i in range(0, len(a)):
        if a[i] == k:
            cnt += 1

    return cnt
