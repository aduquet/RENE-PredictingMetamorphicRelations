def reverse(a):
    r = len(a)
    cnt = 0

    for i in range(len(a) - 1, -1, -1):
        r[cnt] = a[i]
        cnt += 1

    return r
